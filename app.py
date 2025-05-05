import uuid
import boto3
import os
import yaml
from flask import Flask, request, render_template
from datetime import datetime, timezone

# Load configuration from config.yaml
def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

config = load_config()

AWS_REGION = config.get("aws_region")
BUCKET_NAME = config.get("s3_bucket")
TABLE_NAME = config.get("dynamo_table")

# Validate presence of necessary config
if not all([AWS_REGION, BUCKET_NAME, TABLE_NAME]):
    raise EnvironmentError("Missing aws_region, s3_bucket, or dynamo_table in config.yaml.")

# Setup AWS clients (uses default AWS CLI credentials)
s3 = boto3.client("s3", region_name=AWS_REGION)
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

# Optional: print AWS account for debugging
try:
    sts = boto3.client("sts")
    print("✅ Using AWS Account:", sts.get_caller_identity()["Account"])
except Exception:
    print("⚠️ Could not confirm AWS identity (maybe running offline).")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    job_title = request.form.get('job_title')
    resume = request.files.get('resume')

    if not all([name, phone, email, job_title, resume]):
        return "Missing required form data", 400

    resume_filename = f"{name.replace(' ', '_')}_{resume.filename}"
    app_id = str(uuid.uuid4())

    # Upload to S3
    try:
        s3.upload_fileobj(resume, BUCKET_NAME, resume_filename)
    except Exception as e:
        return f"❌ Failed to upload to S3: {str(e)}", 500

    # Save to DynamoDB
    try:
        table.put_item(
            Item={
                'id': app_id,
                'name': name,
                'phone': phone,
                'email': email,
                'job_title': job_title,
                'resume_s3_key': resume_filename,
                'created_at': datetime.now(timezone.utc).isoformat()
            }
        )
    except Exception as e:
        return f"❌ Failed to save to DynamoDB: {str(e)}", 500

    return f"✅ Application received for {name}! Resume uploaded and data saved."

if __name__ == '__main__':
    app.run(debug=True)
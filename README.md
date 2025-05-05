# 🧾 Job Assistance Form App

A full-stack web application that allows users to submit job application details and resumes. The app uploads resumes to **Amazon S3** and stores applicant data in **DynamoDB**, powered by **Flask**, **Pulumi**, and **AWS** services.

---

## 🌐 Features

- Web-based form with fields for name, contact info, job title, and resume upload  
- Resume file stored in **Amazon S3**  
- Application data stored in **Amazon DynamoDB**  
- Infrastructure as Code (IaC) with **Pulumi (Python SDK)**  
- Clean and responsive UI using **HTML/CSS**

---

## 📁 Project Structure

```
.
├── __main__.py           # Pulumi IaC script for provisioning S3 & DynamoDB
├── app.py                # Flask application logic
├── config.yaml           # App config (not included - see below)
├── templates/
│   └── index.html        # HTML form
├── static/
│   └── style.css         # Styling for the form
└── README.md             # Project documentation
```

---

## ⚙️ Tech Stack

- **Frontend**: HTML5, CSS3  
- **Backend**: Flask (Python)  
- **Cloud Services**: AWS S3, DynamoDB  
- **Infrastructure**: Pulumi  
- **Configuration**: YAML  

---

## 🛠️ Prerequisites

- Python 3.7+
- AWS CLI configured with credentials
- Pulumi CLI: [Install Instructions](https://www.pulumi.com/docs/get-started/install/)
- Required Python packages:
  - `boto3`
  - `Flask`
  - `PyYAML`
  - `pulumi`
  - `pulumi-aws`

You can install dependencies using:

```bash
pip install boto3 Flask PyYAML pulumi pulumi-aws
```

Or use a `requirements.txt`:

```text
boto3
Flask
PyYAML
pulumi
pulumi-aws
```

---

## 🧾 Sample `config.yaml`

```yaml
aws_region: us-east-1
s3_bucket: my-bucket-abc123
dynamo_table: my-table
```

Make sure `config.yaml` exists in the root directory before running the Flask app.

---

## 🚀 Getting Started

### 1. Deploy AWS Resources

Run Pulumi to provision infrastructure:

```bash
pulumi up
```

Resources created:
- Amazon S3 bucket
- Amazon DynamoDB table with `id` as the partition key

### 2. Start Flask App

```bash
python app.py
```

Visit: `http://localhost:5000`

---

## 📤 Application Flow

1. User fills out the form and uploads their resume.
2. Resume is uploaded to the specified S3 bucket.
3. Metadata and form data are stored in DynamoDB.
4. Success message is returned.

---

## 🧼 Clean Up

To remove all deployed AWS resources:

```bash
pulumi destroy
```

---

## 🔒 Security Notes

- Make sure to secure your AWS credentials using IAM roles or environment variables.
- For production, disable Flask debug mode and consider using HTTPS and authentication.

---

## ✅ Status & Improvements

**Current Status**: Working Prototype

**Planned Enhancements**:
- Add client-side and server-side validation feedback
- Support email confirmations
- Admin dashboard to view applications
- Authentication and access control

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- Built with [Pulumi](https://www.pulumi.com/)
- Powered by [AWS](https://aws.amazon.com/)
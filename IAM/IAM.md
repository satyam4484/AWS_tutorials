# **AWS Identity and Access Management (IAM) - Overview**  

## **📌 What is IAM?**  
AWS **Identity and Access Management (IAM)** is a service that allows you to securely manage access to AWS resources. With IAM, you can control **who** can access AWS services and **what** actions they can perform.  

## **🔹 Why is IAM Important?**  
- ✅ **Security:** Ensures only authorized users and services access AWS resources.  
- ✅ **Granular Access Control:** Fine-tuned permission management following the *Least Privilege Principle*.  
- ✅ **Centralized User Management:** Easily manage multiple users, groups, and roles.  
- ✅ **Multi-Factor Authentication (MFA):** Enhances security by requiring additional verification.  
- ✅ **Temporary Access:** IAM roles grant short-term access for AWS services without sharing credentials.  

## **🔹 Key IAM Components**  
1. **IAM Users** 👤  
   - Represents individual users with AWS access.  
   - Can have login credentials (username, password, access keys).  
   - Example: A developer who needs access to AWS resources.  

2. **IAM Groups** 🏢  
   - A collection of users with shared permissions.  
   - Simplifies access control by assigning policies to a group instead of individual users.  
   - Example: A "Developers" group with access to EC2 and S3.  

3. **IAM Roles** 🔄  
   - Temporary credentials assigned to users or AWS services.  
   - Best practice: Use IAM roles for AWS services instead of hardcoding access keys.  
   - Example: An EC2 instance that needs to access an S3 bucket.  

4. **IAM Policies** 📜  
   - JSON-based rules that define what actions are allowed or denied.  
   - Can be attached to **users, groups, or roles**.  
   - Example: A policy allowing read-only access to S3.  

## **🔹 Best Practices for IAM**  
✅ Use **IAM roles** for applications instead of access keys.  
✅ Apply the **Principle of Least Privilege** to limit access.  
✅ **Enable Multi-Factor Authentication (MFA)** for extra security.  
✅ **Rotate Access Keys regularly** to prevent unauthorized access.  
✅ Use **AWS CloudTrail** to monitor IAM activity.  


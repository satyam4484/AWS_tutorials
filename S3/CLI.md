
### **1. List Buckets**
```sh
aws s3 ls
```
Lists all S3 buckets in your AWS account.  

### **2. Create a Bucket**  
```sh
aws s3 mb s3://your-bucket-name
```
Creates a new S3 bucket. (Bucket names must be globally unique.)  

### **3. List Objects in a Bucket**  
```sh
aws s3 ls s3://your-bucket-name
```
Lists all objects in the specified S3 bucket.  

### **4. Upload a File to S3**  
```sh
aws s3 cp /path/to/local/file s3://your-bucket-name/
```
Uploads a file to the specified S3 bucket.  

### **5. Download a File from S3**  
```sh
aws s3 cp s3://your-bucket-name/file-name /local/path/
```
Downloads a file from S3 to your local system.  

### **6. Sync a Local Directory to S3**  
```sh
aws s3 sync /local/dir s3://your-bucket-name/
```
Syncs a local directory with an S3 bucket.  

### **7. Delete a File from S3**  
```sh
aws s3 rm s3://your-bucket-name/file-name
```
Deletes a specific file from S3.  

### **8. Delete a Bucket (Empty Bucket Required)**  
```sh
aws s3 rb s3://your-bucket-name
```
Deletes an empty S3 bucket. To delete a non-empty bucket:  
```sh
aws s3 rm s3://your-bucket-name --recursive
aws s3 rb s3://your-bucket-name
```

### **9. Enable Versioning on a Bucket**  
```sh
aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled
```
Enables object versioning on an S3 bucket.  

### **10. Generate a Pre-Signed URL for an Object**  
```sh
aws s3 presign s3://your-bucket-name/object-key --expires-in 3600
```
Generates a temporary URL (valid for 1 hour) to access an S3 object.  

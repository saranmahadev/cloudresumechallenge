# Cloud Resume Challenge

The Cloud Resume Challenge is a hands-on project designed to help you bridge the gap from cloud certification to cloud job. It incorporates many of the skills that real cloud and DevOps engineers use in their daily work.

#### Why doing this?

This project is proposed by [Forrest Brazeal](https://forrestbrazeal.com/) who has lot of experience in cloud and DevOps and it is a great opportunity to learn and practice the skills that you need to be a cloud/devops engineer.

#### Challenge - [🔗](https://cloudresumechallenge.dev/docs/the-challenge/azure/)

### Solution

- Created My GitHub Repository - https://github.com/saranmahadev/cloudresumechallenge
- [Docsify](https://docsify.js.org/getting-started/) is used to generate the docs for my solution 
- For CI/CD created Three Branches
    - Frontend 
    - Backend
    - Docs
- Created my static site using HTML and CSS
- Deployed my static site to Azure Storage using the [Azure CLI](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website-how-to)

<img src="img/files.png" alt="files" style="width:50%">

- Integration with Azure CDN and mapping Subdomain ended in vain because of the limitations of Azure Student Account.

<img src="img/cdn.png" alt="files" style="width:100%">

> Took a lot of time in the Azure Portal but later I got the idea to use Azure CLI to configure CDN.

- GitHub Actions(CI/CD) was created for the Frontend Branch and Whenever a push is made to the Frontend Branch, the Frontend Branch is deployed to Azure Storage,





In this workflow, the Github Actions will run on every push to the main branch. 

The deploy job sets up PHP and installs dependencies. 

It then copies the uploads.tar.gz file to the web server using the scp-action and deploys the code to production using the ssh-deploy action.

After deploying the code, the workflow runs several WP-CLI commands to flush the rewrite rules table, copy the uploads directory to the web server, and replace the legacy URL with the new S3 bucket URL.

Replace the ${{ secrets }} values with your own secrets, and update the deployment script to match your specific Wordpress installation.

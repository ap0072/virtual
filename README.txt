How I hosted my Python Flask Web Application:
-------------------------------------------------

Basic EC2 Hosting:

Using Ec2 server with using public IP + port ( default port as 5000 for Flask Web applications 
Flask app served directly on the default port.

Using Ec2 server with using public IP + Nginx  ( default port as 80) serving with http
Nginx reverse proxy serving Flask app over HTTP

Quick setup for development or testing. Not recommended for production due to lack of security and scalability.


Secure EC2 Hosting:

Using Ec2 server with using public IP + Nginx + certs ( certbot) serving with https
SSL/TLS enabled using Let's Encrypt certificates


Domain Integration:

Using a domain name like mychatbot.sbs and redirecting to Ec2 server using A record pointing to public IP 


Load Balanced Architecture:


Using Ec2 server  with Load balancer + Amazon Certificate Manager + target group 
Application Load Balancer distributes traffic to EC2 instances.
Scalable and secure setup for moderate traffic.


Serverless Architecture:

Using Lambda function + ECR ( Elastic Container Registry ) docker images for simple lightweight applications, Lambda URL handles traffic with https
Flask app containerized and deployed via Lambda.

Using ECS ( Elastic Container Service ) + Load balancer + Auto Scaling group  recommended for Production grade architectures
Containerized Flask app deployed via ECS (Fargate or EC2-backed).





Free Site License:
------------------

CC 3.0 All of the site templates we create for WebThemez are licensed under the Creative Commons Attribution 4.0 License, which means you can:
 - You can use our templates for both personal and commercial projects. 
 - You are NOT allowed to remove the back link to WebThemez.com in templates unless you purchased a license. 
 - You can update /modify/customize the website to fit your project needs. 
 - You cannot claim credit or ownership for any of the files found on webthemez.com. 
 - You cannot redistribute, resell, license, or sub-license any of the files found on webthemez.com. 

 - No Support
 - No Php files ( contact form does not work)
 - No Updates


Credits :
--------- 

=> Design & developed: "WebThemez"  http://webthemez.com 
=> Bootstrap : http://getbootstrap.com/
=> Fontawesome : https://fortawesome.github.io/Font-Awesome/
=> Fonts : https://www.google.com/fonts
=> Images : https://unsplash.com/ , https://www.pexels.com/ and https://pixabay.com/
=> Carousel : http://owlgraphic.com/owlcarousel/

config new site

##install package

*nginx
*python 3
*git
*pip
*virtualenv

like ubuntu,install like:
sudo apt-get install nginx python3 git python3-pip
sudo pip3 install virtualenv

#config nginx

*use template like nginx.template.conf
*replace the SITENAME, use your domin

#upstart task

*use template like upstart.template.conf
*replace the SITENAME, use your domin

##folder 

if you have account, folder is /home/username
/home/username
|__site
   |__SITENAME
      |__database
      |__source
      |__static
      |__virtualenv

 


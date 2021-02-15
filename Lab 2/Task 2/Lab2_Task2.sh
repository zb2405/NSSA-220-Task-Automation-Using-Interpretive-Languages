#!/bin/bash



letter_writer(){
	response=n

	while [[ "$response" != "y" ]]; do
		echo Enter a username:

		read -r "username"

		echo Enter first name:

		read -r "first_name"

		echo Enter last name:

		read -r "last_name"

		echo Department:

		read -r "dept_name"

		echo Job title:

		read -r "job_title"

		useradd "$username"
		

		file_system_writer

		permission_editor

		echo User "$username" added!

		echo Would you like to add another user? '(y/n)'

		read -n1 Input
        
        case $Input in
                [Nn]):
                response="n"
                break;;
        esac

	done

	

}

file_system_writer(){
	mkdir -p /home/"$username"/Desktop
	mkdir -p /home/"$username"/Documents
	mkdir -p /home/"$username"/Downloads
	mkdir -p /home/"$username"/Pictures

	cp ackbar.png /home/"$username"/Pictures/
		
	echo 'Dear '"$first_name"',' >> /home/"$username"/Documents/welcome.txt
	echo 'Welcome to Initech Corporation! We’re so happy to have you in the '"$dept_name"' Department as a '"$job_title"'. Please' >> /home/"$username"/Documents/welcome.txt
	echo 'don’t forget to complete your TPS Reports in a timely manner.' >> /home/"$username"/Documents/welcome.txt
	echo 'Sincerely,' >> /home/"$username"/Documents/welcome.txt
	echo 'Bill Lumbergh' >> /home/"$username"/Documents/welcome.txt

}

permission_editor(){
	chmod 644 /home/"$username"/Pictures/ackbar.png
	chmod 444 /home/"$username"/Documents/welcome.txt

}

letter_writer




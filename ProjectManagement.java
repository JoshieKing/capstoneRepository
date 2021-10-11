import java.util.Scanner;

public class ProjectManagement {

	public static void main(String[] args) {
		/* creating the booleans for the while loops
		 * creating the scanner object
		 * creating the objects for projects, architects, etc
		 * printing out all the details for the objects*/
		boolean projectChanges = true;
		boolean contractorChanges = true;
		boolean architectChanges = true;
		boolean customerChanges = true;
		
		Scanner changes = new Scanner(System.in);
		
		NewProject firstProject = new NewProject(1, "First Project", "Apartment",
				"3 Sunningdale Avenue", 987, 150264.89, 20000, "15 February 2022");
		
		Contractor sam = new Contractor("Sam", "012 654 7848", "contractorssam@gmail.com",
				"23 Watermelon Drive");
		
		Architect bethany = new Architect("Bethany", "013 547 7844", "architectbeth@gmail.com",
				"23 Watermelon Drive");
		
		Customer matt = new Customer("Matthew", "084 745 4878", "mattstevens@yahoo.com",
				"462 Leukemia Road");
		
		System.out.println("\tProjects\n");
		System.out.println(firstProject);
		
		System.out.println("\n\tContractors\n");
		System.out.println(sam);
		
		System.out.println("\n\tArchitects\n");
		System.out.println(bethany);
		
		System.out.println("\n\tCustomer\n");
		System.out.println(matt);
		
		// while loop to allow the user to make as many changes as they want
		while(projectChanges) {
			
			/* provides a display of all the changes the user can make
			 * or to confirm all the changes*/
			System.out.println("\nWould you like to change any of the following (Please enter as shown below):");
			System.out.println("\tDeadline\n" + "\tTotal paid");
			System.out.println("To confirm all details enter 'confirm'");
			
			String userChanges = changes.nextLine();
			
			/* if the user enters any of the possible changes they can make
			 * they are asked what they want to change the chosen field to
			 * after they make the change all the details are displayed again
			 * if they have completed any changes they want or don't want to change anything
			 * they can enter confirm to stop the while loop*/
			if (userChanges.equals("Deadline")) {
				System.out.println("What do you want the new deadline to be:");
				firstProject.projectDeadline = changes.nextLine();
				System.out.println(firstProject);
			}
			else if (userChanges.equals("Total paid")) {
				System.out.println("How much has been paid in total so far:");
				firstProject.totalPaid = changes.nextDouble();
				System.out.println(firstProject);
			}
			else if (userChanges.equals("confirm")) {
				projectChanges = false;
			}
		}
		
		// while loop to allow the user to make as many changes as they want
		while(contractorChanges) {
			
			/* provides a display of all the changes the user can make
			 * or to confirm all the changes*/
			System.out.println("\nWould you like to change any of the following for a contractor"
					+ "(Please enter as shown below):");
			System.out.println("\tName\n" + "\tTelephone number\n" +
					"\tEmail address\n" + "\tPhysical Address");
			System.out.println("To confirm all details enter 'confirm'");
			
			String userChanges = changes.nextLine();
			
			/* if the user enters any of the possible changes they can make
			 * they are asked what they want to change the chosen field to
			 * after they make the change all the details are displayed again
			 * if they have completed any changes they want or don't want to change anything
			 * they can enter confirm to stop the while loop*/
			if (userChanges.equals("Name")) {
				System.out.println("What do you want to change the name to:");
				sam.name = changes.nextLine();
				System.out.println(sam);
			}
			else if (userChanges.equals("Telephone number")) {
				System.out.println("What do you want to change the number to:");
				sam.telephoneNumber = changes.nextLine();
				System.out.println(sam);
			}
			else if (userChanges.equals("Email address")) {
				System.out.println("what do you want to change the email address to:");
				sam.emailAddress = changes.nextLine();
				System.out.println(sam);
			}
			else if (userChanges.equals("Physical Address")) {
				System.out.println("What do you want to change the physical address to:");
				sam.physicalAddress = changes.nextLine();
				System.out.println(sam);
			}
			else if (userChanges.equals("confirm")) {
				contractorChanges = false;
			}
		}
		
		// while loop to allow the user to make as many changes as they want
		while(architectChanges) {
			
			/* provides a display of all the changes the user can make
			 * or to confirm all the changes*/
			System.out.println("\nWould you like to change any of the following for an architect"
					+ "(Please enter as shown below):");
			System.out.println("\tName\n" + "\tTelephone number\n" +
					"\tEmail address\n" + "\tPhysical Address");
			System.out.println("To confirm all details enter 'confirm'");
			
			String userChanges = changes.nextLine();
			
			/* if the user enters any of the possible changes they can make
			 * they are asked what they want to change the chosen field to
			 * after they make the change all the details are displayed again
			 * if they have completed any changes they want or don't want to change anything
			 * they can enter confirm to stop the while loop*/
			if (userChanges.equals("Name")) {
				System.out.println("What do you want to change the name to:");
				bethany.name = changes.nextLine();
				System.out.println(bethany);
			}
			else if (userChanges.equals("Telephone number")) {
				System.out.println("What do you want to change the number to:");
				bethany.telephoneNumber = changes.nextLine();
				System.out.println(bethany);
			}
			else if (userChanges.equals("Email address")) {
				System.out.println("what do you want to change the email address to:");
				bethany.emailAddress = changes.nextLine();
				System.out.println(bethany);
			}
			else if (userChanges.equals("Physical Address")) {
				System.out.println("What do you want to change the physical address to:");
				bethany.physicalAddress = changes.nextLine();
				System.out.println(bethany);
			}
			else if (userChanges.equals("confirm")) {
				architectChanges = false;
			}
		}
		
				// while loop to allow the user to make as many changes as they want
				while(customerChanges) {
					
					/* provides a display of all the changes the user can make
					 * or to confirm all the changes*/
					System.out.println("\nWould you like to change any of the following for an customer"
							+ "(Please enter as shown below):");
					System.out.println("\tName\n" + "\tTelephone number\n" +
							"\tEmail address\n" + "\tPhysical Address");
					System.out.println("To confirm all details enter 'confirm'");
					
					String userChanges = changes.nextLine();
					
					/* if the user enters any of the possible changes they can make
					 * they are asked what they want to change the chosen field to
					 * after they make the change all the details are displayed again
					 * if they have completed any changes they want or don't want to change anything
					 * they can enter confirm to stop the while loop*/
					if (userChanges.equals("Name")) {
						System.out.println("What do you want to change the name to:");
						matt.name = changes.nextLine();
						System.out.println(matt);
					}
					else if (userChanges.equals("Telephone number")) {
						System.out.println("What do you want to change the number to:");
						matt.telephoneNumber = changes.nextLine();
						System.out.println(matt);
					}
					else if (userChanges.equals("Email address")) {
						System.out.println("what do you want to change the email address to:");
						matt.emailAddress = changes.nextLine();
						System.out.println(matt);
					}
					else if (userChanges.equals("Physical Address")) {
						System.out.println("What do you want to change the physical address to:");
						matt.physicalAddress = changes.nextLine();
						System.out.println(matt);
					}
					else if (userChanges.equals("confirm")) {
						customerChanges = false;
					}
				}
	}
}


public class Contractor {
		// Attributes
	String name;
	String telephoneNumber;
	String emailAddress;
	String physicalAddress;
	
		// Methods
	// creating contractor object
	public Contractor(String name, String telephoneNumber,
			String emailAddress, String physicalAddress) {
		this.name = name;
		this.telephoneNumber = telephoneNumber;
		this.emailAddress = emailAddress;
		this.physicalAddress = physicalAddress;
	}
	
	// printing the contractor object information
	public String toString() {
		String output = "Contractor name: " + name;
		output += "\nContractor's telephone number: " + telephoneNumber;
		output += "\nContractor's email address: " + emailAddress;
		output += "\nContractor's physical address: " + physicalAddress;
		
		return output;
	}
}

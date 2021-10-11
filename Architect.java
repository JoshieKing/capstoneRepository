
public class Architect {
		// Attributes
	String name;
	String telephoneNumber;
	String emailAddress;
	String physicalAddress;
	
		// Methods
	// creating architect object
	public Architect(String name, String telephoneNumber,
			String emailAddress, String physicalAddress) {
		this.name = name;
		this.telephoneNumber = telephoneNumber;
		this.emailAddress = emailAddress;
		this.physicalAddress = physicalAddress;
	}
	
	// printing the architect object information
	public String toString() {
		String output = "Architect name: " + name;
		output += "\nArchitect's telephone number: " + telephoneNumber;
		output += "\nArchitect's email address: " + emailAddress;
		output += "\nArchitect's physical address: " + physicalAddress;
		
		return output;
	}
}

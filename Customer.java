
public class Customer {
		// Attributes
	String name;
	String telephoneNumber;
	String emailAddress;
	String physicalAddress;
	
		// Methods
	// creating customer object
	public Customer(String name, String telephoneNumber,
			String emailAddress, String physicalAddress) {
		this.name = name;
		this.telephoneNumber = telephoneNumber;
		this.emailAddress = emailAddress;
		this.physicalAddress = physicalAddress;
	}
	
	// printing the customer object information
	public String toString() {
		String output = "Customer name: " + name;
		output += "\nCustomer's telephone number: " + telephoneNumber;
		output += "\nCustomer's email address: " + emailAddress;
		output += "\nCustomer's physical address: " + physicalAddress;
		
		return output;
	}
}

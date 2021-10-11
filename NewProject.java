
public class NewProject {
		// Attributes
	int projectNumber;
	String projectName;
	String buildingType;
	String physicalAddress;
	int erfNumber;
	double totalFee;
	double totalPaid;
	String projectDeadline;
	
		// Methods
	// Used to create project objects
	public NewProject(int projectNumber, String projectName, String buildingType,
			String physicalAddress, int erfNumber, double totalFee,
			double totalPaid, String projectDeadline) {
		this.projectNumber = projectNumber;
		this.projectName = projectName;
		this.buildingType = buildingType;
		this.physicalAddress = physicalAddress;
		this.erfNumber = erfNumber;
		this.totalFee = totalFee;
		this.totalPaid = totalPaid;
		this.projectDeadline = projectDeadline;
	}
	
	public String toString() {
		String output = "Project Number: " + projectNumber;
		output += "\nProject Name " + projectName;
		output += "\nBuilding's Type: " + buildingType;
		output += "\nPhysical Address of building: " + physicalAddress;
		output += "\nBuilding ERF Number: " + erfNumber;
		output += "\nTotal Fee for building: " + totalFee;
		output += "\nTotal Paid already: " + totalPaid;
		output += "\nProject Completion Deadline: " + projectDeadline;
		
		return output;
	}	
}

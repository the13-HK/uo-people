package paunit2;

class BookInfo {
	private String name;
	private String author;
	private int quantity;

	public BookInfo(String name, String author, int quantity) {
		// TODO Auto-generated constructor stub
		this.name = name;
		this.author = author;
		this.quantity = quantity;
	}
	
	public String getName() {
		return this.name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public String getAuthor() {
		return this.author;
	}
	
	public void setAuthor(String author) {
		this.author = author;
	}
	
	public int getQuantity() {
		return this.quantity;
	}
	
	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}

}

package paunit2;

import java.util.List;
import java.util.ArrayList;

class Library {
	private List<BookInfo> stock;

	public Library() {
		// TODO Auto-generated constructor stub
		this.stock= new ArrayList<BookInfo>();
	}
	
	public void addBook(String name, String author) {
		int size = stock.size();
		boolean changeFlg = false;
		for (int i=0; i < size; i++) {
			BookInfo book = stock.get(i);
			if (book.getName().equals(name) && book.getAuthor().equals(author)) {
				int presentQuantity = book.getQuantity();
				book.setQuantity(presentQuantity + 1);
				stock.set(i, book);
				changeFlg = true;
				System.out.println("Inventory has increased!");
				System.out.println("Book name is " + book.getName()+ "/ Author is " + book.getAuthor()+ "/ present quantity is " + book.getQuantity());
				break;
			}
		}
		if (!changeFlg) {
			BookInfo newBook = new BookInfo(name, author, 1);				
			stock.add(newBook);
			System.out.println("Added new book!!");
			System.out.println("Book name is " + newBook.getName()+ "/ Author is " + newBook.getAuthor()+ "/ present quantity is " + newBook.getQuantity());
		}
	}

	public void borrowBook(String name, String author) {
		int size = stock.size();
		boolean changeFlg = false;
		for (int i=0; i < size; i++) {
			BookInfo book = stock.get(i);
			if (book.getName().equals(name) && book.getAuthor().equals(author)) {
				int presentQuantity = book.getQuantity();
				if (presentQuantity >= 1) {
					book.setQuantity(presentQuantity - 1);
					stock.set(i, book);
					changeFlg = true;
					System.out.println("I lent it!");
					System.out.println("Book name is " + book.getName()+ "/ Author is " + book.getAuthor()+ "/ present quantity is " + book.getQuantity());
				}else {
					System.out.println("Out of stock!");
					changeFlg = true;
				}
				break;
			}
		}
		if (!changeFlg) {
			System.out.println("Could not lend");
		}
	}
	
	public void returnBook(String name, String author) {
		int size = stock.size();
		boolean changeFlg = false;
		for (int i=0; i < size; i++) {
			BookInfo book = stock.get(i);
			if (book.getName().equals(name) && book.getAuthor().equals(author)) {
				int presentQuantity = book.getQuantity();
				book.setQuantity(presentQuantity + 1);
				stock.set(i, book);
				changeFlg = true;
				System.out.println("Returned!");
				System.out.println("Book name is " + book.getName()+ "/ Author is " + book.getAuthor()+ "/ present quantity is " + book.getQuantity());
			}
		}
		if (!changeFlg) {
			System.out.println("Could not return...");
		}
		
		
	}

}

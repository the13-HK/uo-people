package paunit2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.regex.Pattern;

public class Main {
	private static BufferedReader userInputStreamReader;
    static {                  
	userInputStreamReader = new BufferedReader(new InputStreamReader(System.in)); 
    }
	
	/** System.in (通常キーボード) から1行読み込む */
    private static String readLine() {
	String inputString = "";         // エラー時には null ではなく "" になる
	try {
	    inputString = userInputStreamReader.readLine();
	}
	catch (Exception e) {
	    e.printStackTrace();
	}
	return inputString;
    }

	public Main() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Library testLibrary = new Library(); 
		System.out.println("init!");
		String action;
		String bookName;
		String authorName;
		String actionRegex = "Add|Borrow|Return";
		Pattern actionPattern = Pattern.compile(actionRegex);
		
		while (true) {
			System.out.println("Please Input Your Action, Add or Borrow, Return. if you want end, please input exit");
			action = readLine();
	    	// Validate Check
		    if(actionPattern.matcher(action).find()) {
		    	System.out.println("Please Input book name");
		    	bookName = readLine();
		    	System.out.println("Please Input author name");
		    	authorName = readLine();
		    	switch (action) {
		    	case "Add":
		    		testLibrary.addBook(bookName, authorName);
		    		break;
		    	case "Borrow":
		    		testLibrary.borrowBook(bookName, authorName);
		    		break;
		    	case "Return":
		    		testLibrary.returnBook(bookName, authorName);
		    		break;
		    	}
		    }else {
		    	if(action.equals("exit")){
		    		System.out.println("End!!!!!");
		    		break;
		    	}else {
			    	System.out.println("Your input is wrong. Please retry");
			    	continue;
		    	}
		    }
		};
	}

}

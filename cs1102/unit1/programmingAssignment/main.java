package programmingAssignment;

import java.io.*;
import java.util.regex.*;

public class main {

	public main() {
		// TODO Auto-generated constructor stub
	}

	private static BufferedReader userInputStreamReader;
	static {
		userInputStreamReader = new BufferedReader(new InputStreamReader(System.in));
	}

	/** System.in (通常キーボード) から1行読み込む */
	private static String readLine() {
		String inputString = ""; // エラー時には null ではなく "" になる
		try {
			inputString = userInputStreamReader.readLine();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return inputString;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String line;
		String[][] question_list = new String[5][3];
		question_list[0][0] = "What is the answer to 81 + 18 ?";
		question_list[0][1] = "A: 98, B: 99, C: 100, D:101 ";
		question_list[0][2] = "B";

		question_list[1][0] = "What is the answer to 25*25?";
		question_list[1][1] = "A: 425, B: 525, C: 625, D:725";
		question_list[1][2] = "C";

		question_list[2][0] = "What is the answer to 94 - 76?";
		question_list[2][1] = "A: 18, B: 8, C: 28, D:16 ";
		question_list[2][2] = "A";

		question_list[3][0] = "What is the answer to 144 / 12 ?";
		question_list[3][1] = "A: 10, B: 11, C: 12, D:3 ";
		question_list[3][2] = "CSSSSS";

		question_list[4][0] = "What is the answer to 100 + 16 * 2 ?";
		question_list[4][1] = "A: 232, B: 242, C: 122, D:132 ";
		question_list[4][2] = "D";

		String[] answer_list = new String[5];
		String regex = "A|B|C|D";
		Pattern p = Pattern.compile(regex);
		Boolean answer_flg;

		for (int i = 0; i < question_list.length; i++) {
			System.out.println(question_list[i][0]);
			System.out.println(question_list[i][1]);
			answer_flg = false;
			while (!answer_flg) {
				line = readLine();
				if (p.matcher(line).find()) {
					answer_list[i] = line;
					answer_flg = true;
				} else {
					System.out.println("Your input is wrong. Please Input A or B or C or D");
					continue;
				}
			}
		}

		for (int i = 0; i < question_list.length; i++) {
			if (answer_list[i].equals(question_list[i][2])) {
				System.out.println("Question" + i + "is Correct!!!");
			} else {
				System.out.println("Question" + i + 1 + "is Wrong....");
			}
		}
	}

}

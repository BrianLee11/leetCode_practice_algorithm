package q1_twoSum;

public class LeetCode13RomanToInteger {

	public int romanToInt(String s) {
		
		// initialize variables
		int i = 0;
		int n = s.length();
		int number = 0; 
		
		while (i < n) {
			
			// Case 1:
			if (s.charAt(i) == 'I') {
				
				// checking for IV or IX
				if (i+1 < n) {
					
					if (s.charAt(i+1) == 'V') {
						number += 4; 
						i += 2; 
						continue;
					}
					
					else if (s.charAt(i+1) == 'X') {
						number += 9;
						i += 2;
						continue;
					}
					
					// at least two digits remain, but not IV nor IX
					else number += 1;
				} // end of checking for IV or IX 
				
				// only one digit remain
				else number += 1;
				
			} // end of case I: 'I'
			
			// Case 2: starts with 'X'
			if (s.charAt(i) == 'X' ) {
				
				// check for XL and XC
				if (i+1 < n) {
					
					if (s.charAt(i+1) == 'L') {
						number += 40;
						i += 2;
						continue;						
					}
					
					else if (s.charAt(i+1) == 'C') {
						number += 90;
						i += 2;
						continue;
					}
					
					// has at least 2 digits, but not XL nor XC
					else number += 10;
					
				} // end of checking for XL and XC
				
				// one digit remaining
				else number += 10;
				
			} // end of starting with 'X'
			
			// Case 3: starts with 'C'
			if (s.charAt(i) == 'C') {
				
				// checking for CD or CM
				// check validity: at least two digits remain
				if (i+1 < n) {
					
					// CD
					if (s.charAt(i+1) == 'D') {
						number += 400;
						i += 2;
						continue;
					}
					
					// CM
					if (s.charAt(i+1) == 'M') {
						number += 900;
						i += 2;
						continue;
					}
					
					// two digits, but neither CD nor CM
				else number += 100;
					
				}// end of checking for CD or CM
				
				// one digit remaining
				else number += 100;
				
			} // end of Case 3: starts with 'C'
			
			// the rest letters: V, L, D, M
			if (s.charAt(i) == 'V') number += 5;
			if (s.charAt(i) == 'L') number += 50;
			if (s.charAt(i) == 'D') number += 500;
			if (s.charAt(i) == 'M') number += 1000;
			
			// increment i by one
			i += 1;
		}
		return number;
    }
	

	// main method inside the class
    public static void main(String[] args) {
    	LeetCode13RomanToInteger solver = new LeetCode13RomanToInteger();
        String string1 = "III";
        int result = solver.romanToInt(string1);
        System.out.println(result); // III should be 3
        
        String string2 = "LVIII"; 
        int result2 = solver.romanToInt(string2);
        System.out.println(result2); // should be 58
        
        String string3 = "MCMXCIV"; 
        int result3 = solver.romanToInt(string3);
        System.out.println(result3); //should be 1994
        
    }
}

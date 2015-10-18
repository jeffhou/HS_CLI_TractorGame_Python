package tractor;

import java.util.List;

public class Util {

	public static boolean isSubSet(List<?> sortedSubList, List<?> sortedSuperList) {
		int j = 0;
		for (int i = 0; i < sortedSubList.size(); i++){
			boolean notSubset = false;
			while(true) {
				//System.out.println("Comparing " + sortedSubList.get(i) + " (i="+i+") with " + sortedSuperList.get(j) + "(j="+j+") ");
				if(sortedSubList.get(i).equals(sortedSuperList.get(j))){
					j++;
					//System.out.println("EQUAL");
					break;
				}
				//System.out.println("UNEQUAL");
				j++;
				if(j >= sortedSuperList.size()){
					notSubset = true;
					break;
				}
			}
			if (notSubset || j == sortedSuperList.size()) {
				//System.out.println("RETURNING FALSE");
				return false;
			}
			
		}
		System.out.println("RETURNING TRUE");
		return true;
	}

}

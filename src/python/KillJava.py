"""
package tractor;

import java.io.IOException;

public class KillJava {
	public static void main(String[] args) throws IOException {
		@SuppressWarnings("unused")
		Process p = new ProcessBuilder("taskkill.exe", "/F", "/IM", "javaw.exe").start();
	}
}
"""
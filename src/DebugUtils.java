
public class DebugUtils {
	public static int verbosity = 0;
	static void notice(String debugMessage, int verbosityMinimum) {
		if (verbosityMinimum <= verbosity) {
			System.out.println(debugMessage);
		}
	}
}

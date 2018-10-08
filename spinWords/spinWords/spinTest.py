import unittest
import spinWords as sw

class Test_spinTest(unittest.TestCase):
	def test1(test):
		result = sw.spin_words("Welcome")
		test.assertEquals(result, "emocleW", "{} was not emocleW".format(result))

	def test2(test):
		result = sw.spin_words("h")
		test.assertEquals(result, "h", "{} was not h".format(result))

	def test3(test):
		result = sw.spin_words("This is a test sentence")
		test.assertEquals(result, "This is a test ecnetnes", "output was not as expected")

	def test4(test):
		result = sw.spin_words("The predominant quantity of words are greater than five letters")
		test.assertEquals(result, "The tnanimoderp ytitnauq of sdrow are retaerg than five srettel", "output was not as expected")

if __name__ == '__main__':
	unittest.main()

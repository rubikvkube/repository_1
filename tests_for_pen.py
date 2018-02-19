import unittest
import sys
import os
import Pen as p
from ddt import ddt, data, unpack

@ddt
class TestCasesForPen(unittest.TestCase):
	
#Check _init_
	def test_init_default_ink_container_value(self):
		pen = p.Pen()
		self.assertEqual(pen.ink_container_value, 1000, msg = 'ink_container_value should be equal to 1000')

	def test_init_negative_ink_container_value(self):
		pen = p.Pen(ink_container_value=-5)
		self.assertEqual(pen.ink_container_value, 0, msg = 'ink_container_value should be equal to 0 as specified argument is negative')

	def test_init_invalid_ink_container_value(self):
		self.assertRaises(ValueError, p.Pen, ink_container_value='asas')

	def test_init_default_size_letter(self):
		pen = p.Pen()
		self.assertEqual(pen.size_letter, 1.0, msg = 'size_letter should be equal to 1.0')

	@data (2, 4.0, 0, -2)
	def test_init_size_letter_int(self, value):
		pen = p.Pen(size_letter=value)
		if value > 0:
			self.assertEqual(pen.size_letter, float(value), msg = 'size_letter should be equal to %s' % (value))
		else:
			self.assertEqual(pen.size_letter, 0,  msg = 'size_letter should be equal to 0 as specified argument <= 0')

	def test_init_invalid_size_letter(self):
		self.assertRaises(ValueError, p.Pen, size_letter='asas')

	def test_init_default_color(self):
		pen = p.Pen()
		self.assertEqual(pen.color, 'blue', msg = 'color should be blue')

	def test_init_invalid_color(self):
		self.assertRaises(ValueError, p.Pen, color=25)


#Check get_color
	@data ('blue', 'red', 'white', 'green')
	def test_get_color_should_return_color(self, color):
		pen=p.Pen()
		pen.color=color
		self.assertEqual(pen.get_color(), color, msg = 'color should be %s' % (color))


#Check check_pen_state is True
	@data (1000, 10, 0.5)
	def test_check_pen_state_should_return_true(self, value):
		pen=p.Pen(ink_container_value=value, size_letter=2.0, color='red')
		self.assertTrue(pen.check_pen_state(), msg = 'True should be returned as specified argument is greater than 0')

#Check check_pen_state is False
	@data (-10, 0)
	def test_check_pen_state_should_return_false(self, value):
		pen=p.Pen(ink_container_value = value, size_letter=2.0, color='red')
		self.assertFalse(pen.check_pen_state(), msg = 'False should be returned as specified argument is not greater than 0')

	
#Check do_something_else
	def test_do_something_else_should_return_red(self):
		pen = p.Pen(color='red')                
		sys.stdout = open('.\\file.txt', "w") 
		pen.do_something_else()
		sys.stdout.close()                               
		f = open('.\\file.txt', "r")
		a = f.read()
		f.close()
		os.remove('.\\file.txt')
		self.assertEqual(a, "red\n", msg = 'do_something_else method should return \'red')


#Check write
	@data (-5, 0)
	def test_write_should_return_nothing(self, value):
		"""ink_container_value < 0 and ink_container_value = 0"""
		pen=p.Pen(ink_container_value = value)
		self.assertEqual(pen.write('pen'), "", msg = 'nothing should be returned as ink_container_value <= 0')

	def test_write_should_return_word(self):
		"""size_of_word < ink_container_value"""
		pen=p.Pen(size_letter=2.0, ink_container_value=15)
		self.assertEqual(pen.write('python'), "python", msg = 'whole word should be returned as ink_container_value > size_of_word')
		self.assertEqual(pen.ink_container_value, 3.0)

	def test_write_should_return_word(self):
		"""size_of_word = ink_container_value"""
		pen=p.Pen(ink_container_value=3)
		self.assertEqual(pen.write('pen'), "pen", msg = 'whole word should be returned as size_of_word = ink_container_value')
		self.assertEqual(pen.ink_container_value, 0.0)

	def test_write_should_return_part_of_word(self):
		"""size_of_word > ink_container_value"""
		pen=p.Pen(size_letter=2, ink_container_value=10)
		self.assertEqual(pen.write('python'), "pytho", msg = 'part of word should be returned as ink_container_value < size_of_word > ')
		self.assertEqual(pen.ink_container_value, 0.0)




suite = unittest.TestLoader().loadTestsFromTestCase(TestCasesForPen)
unittest.TextTestRunner(verbosity=2).run(suite)
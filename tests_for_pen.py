import unittest
import sys
import Pen as p

class TestCasesForPen(unittest.TestCase):
	
#Check _init_

	def test01_init_valid_ink_container_value(self):
		new_object = p.Pen()
		self.assertEqual(new_object.ink_container_value, 1000)

	def test02_init_negative_ink_container_value(self):
		new_object = p.Pen(ink_container_value=-5)
		self.assertEqual(new_object.ink_container_value, 0)

	def test03_init_invalid_ink_container_value(self):
		self.assertRaises(ValueError, p.Pen, ink_container_value='asas')

	def test04_init_valid_size_letter(self):
		new_object = p.Pen()
		self.assertEqual(new_object.size_letter, 1.0)

	def test05_init_valid_size_letter_int(self):
		new_object = p.Pen(size_letter=2)
		self.assertEqual(new_object.size_letter, 2.0)
		
	def test06_init_negative_size_letter(self):
		new_object = p.Pen(size_letter=-2.0)
		self.assertEqual(new_object.size_letter, 0)

	def test07_init_invalid_size_letter(self):
		self.assertRaises(ValueError, p.Pen, size_letter='asas')

	def test08_init_valid_color(self):
		new_object = p.Pen()
		self.assertEqual(new_object.color, 'blue')

	def test09_init_invalid_color(self):
		self.assertRaises(ValueError, p.Pen, color=25)


#Check get_color

	def test10_get_color_should_return_blue(self):
		new_object=p.Pen()
		self.assertEqual(new_object.get_color(), 'blue')


	def test11_get_color_should_return_red(self):
		new_object=p.Pen()
		new_object.color='red'
		self.assertEqual(new_object.get_color(), 'red')


#Check check_pen_state is True

	def test12_check_pen_state_should_return_True(self):
		new_object=p.Pen()
		self.assertTrue(new_object.check_pen_state())

	def test13_check_pen_state_should_return_True(self):
		new_object=p.Pen(ink_container_value=10, size_letter=2.0, color='red')
		self.assertTrue(new_object.check_pen_state())

	def test14_check_pen_state_should_return_True(self):
		new_object=p.Pen(ink_container_value=0.5)
		self.assertTrue(new_object.check_pen_state())

#Check check_pen_state is False

	def test15_check_pen_state_should_return_False(self):
		new_object=p.Pen(ink_container_value=-10)
		self.assertFalse(new_object.check_pen_state())

	def test16_check_pen_state_should_return_False(self):
		new_object=p.Pen(ink_container_value=0, size_letter=2.0, color='red')
		self.assertFalse(new_object.check_pen_state())

	
#Check do_something_else
	def test17_do_something_else_should_return_red(self):
		new_object = p.Pen(color='red')
		temp = sys.stdout                 
		sys.stdout = open('.\\file.txt', "w") 
		new_object.do_something_else()
		sys.stdout.close()                
		sys.stdout = temp                 
		file=open('.\\file.txt', "r") 
		self.assertEqual(file.read(),"red\n")


#Check write
	def test18_write_should_return_nothing(self):  #ink_container_value < 0
		new_object=p.Pen(ink_container_value=-5)
		self.assertEqual(new_object.write('pen'), "")

	def test19_write_should_return_nothing(self):  #ink_container_value = 0
		new_object=p.Pen(ink_container_value=0)
		self.assertEqual(new_object.write('pen'), "")

	def test20_write_should_return_word(self):  # size_of_word < ink_container_value
		new_object=p.Pen(size_letter=2.0, ink_container_value=15)
		self.assertEqual(new_object.write('python'), "python")
		self.assertEqual(new_object.ink_container_value, 3.0)

	def test21_write_should_return_word(self):  # size_of_word = ink_container_value
		new_object=p.Pen(ink_container_value=3)
		self.assertEqual(new_object.write('pen'), "pen")
		self.assertEqual(new_object.ink_container_value, 0.0)

	def test22_write_should_return_part_of_word(self):  # size_of_word > ink_container_value
		new_object=p.Pen(size_letter=2, ink_container_value=10)
		self.assertEqual(new_object.write('python'), "pytho")
		self.assertEqual(new_object.ink_container_value, 0.0)




suite = unittest.TestLoader().loadTestsFromTestCase(TestCasesForPen)
unittest.TextTestRunner(verbosity=2).run(suite)
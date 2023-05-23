import unittest
from python_chat_with_ChatGPT import get_response, check_response

def test(query):
    #print(query)
    GPT_response = get_response(query)
    try:
        #print(f"original response:{GPT_response}")
        msg = GPT_response['choices'][0]['text']
        check = check_response(query, msg)
        return check
    except:
    	return False

class TestQueryResponse(unittest.TestCase):

	def test_travel_1(self):
		query = "Is there public transport available?"
		self.assertTrue(test(query))

	def test_travel_2(self):
		query = "How convenient is it to get between places?"
		self.assertTrue(test(query))

	def test_travel_3(self):
		query = "What are some tourist attractions there?"
		self.assertTrue(test(query))

	def test_food_1(self):
		query = "What are the best restaurants to go to?"
		self.assertTrue(test(query))

	def test_food_2(self):
		query = "What are some local dishes to try out?"
		self.assertTrue(test(query))

	def test_food_3(self):
		query = "How many meals will I be having?"
		self.assertTrue(test(query))

	def test_accommodation_1(self):
		query = "What are the most affordable places to stay at?"
		self.assertTrue(test(query))

	def test_accommodation_2(self):
		query = "What are some cheaper alternatives to staying at hotels?"
		self.assertTrue(test(query))

if __name__ == '__main__':
	unittest.main()

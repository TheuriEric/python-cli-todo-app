import unittest
from unittest.mock import patch, mock_open,MagicMock #input() open() print()
import json
from utils import load_tasks, add_tasks

###Tests for functions :
#   load_tasks()
#   save_tasks()
dummy_data = {
    "id": 1,
    "title": "Sample task",
    "description" : "This is a sample task for testing",
    "due_date" : "2025-07-01",
    "completed" : "Incomplete"
} ##This will be our sample data, as if we have actually input the values by ourselves

class TestLoadTasks(unittest.TestCase):
    @patch("builtins.print") #simulates the print function
    @patch("builtins.open",new_callable=mock_open,read_data=json.dumps([dummy_data])) #simulates the open and read write methods

    def test_load_tasks_print_tasks(self,mock_file,mock_print):
        tasks = load_tasks()
        mock_file.assert_called_once_with("tasks.json","r")#ensures correct file opening

        self.assertEqual(len(tasks),1) #Ensures a task is provided
        self.assertEqual(tasks[0]["title"],"Sample task")  #title of the task is 'Sample task'

        mock_print.assert_any_call("Here are all the tasks:\n") #Ensures the line is printed
        self.assertTrue(any("Sample task" in str(call) for call in mock_print.call_args_list))

class TestAddTasks(unittest.TestCase):
    @patch("builtins.input",side_effect=[
        "1","Sample task","This is a sample task for testing","y","2020-12-12"
    ])#simulates the input method and gets the inputs in the order provided
    @patch("os.path.exists",return_value=False)#assumes tasks is nonesistent
    @patch("builtins.open",new_callable=mock_open)#checks the file opened
    @patch("builtins.print")#mocks the print method
    def test_add_tasks_creates_task(self,mock_print,mock_file,mock_exists,mock_input):
        add_tasks()#The actual function is called
        mock_file.assert_called_with("tasks.json","w")#Ensures the file was opened in write mode
        handle = mock_file() ##Gives the file-like object being used
        written_data = "".join(call.args[0] for call in handle.write.call_args_list)#Collects all the .write() calls made to the file and puts them in a string 
        saved = json.loads(written_data)#Convert the JSON string to a Python list

        self.assertEqual(saved[0]['title'], "Sample task")
        self.assertEqual(saved[0]['completed'], "Incomplete")
        self.assertEqual(saved[0]["due_date"],"2020-12-12")#Confirms correct information

        mock_print.assert_any_call("Successfully created task")#Confirms the success message was called


if __name__ == "__main__":
    unittest.main()

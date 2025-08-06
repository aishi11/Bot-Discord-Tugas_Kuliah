from commands import TaskBot

def test_list_tasks(capsys):
    bot = TaskBot()
    bot.add_task("Task to list")
    bot.list_tugas()
    captured = capsys.readouterr()
   

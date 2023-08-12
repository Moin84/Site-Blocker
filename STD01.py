import win32com.client

def STD01(x):
    TriggerTypeDaily = 2
    ActionTypeExec = 0

    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')
    task_def = scheduler.NewTask(0)

    task_def.RegistrationInfo.Description = "Block time settings"

    task_def.Settings.Enabled = True
    task_def.settings.StartWhenAvailable = True
    task_def.settings.Hidden = False
    task_def.settings.DisallowStartIfOnBatteries = False

    trigger = task_def.Triggers.create(TriggerTypeDaily)

    trigger.StartBoundary = x
    trigger.DaysInterval = 1
    trigger.Id = "DailyTriggerId"
    trigger.Enabled = True

    Action = task_def.Actions.Create( ActionTypeExec )
    Action.Path = "D:\Projects\Project Files\SiteBlocker\Block_1.exe"

    root_folder.RegisterTaskDefinition(
        "BlockSTD01", task_def, 6, "", "", 3)

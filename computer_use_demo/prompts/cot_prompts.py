# Chain-of-Thought Prompts

class COT_PROMPTS:

    @classmethod
    def planning_prompt(cls, user_task: str):
        return f'''Using what is currently on the screen, come up with at most 5 steps to perform the following task. The less number of steps the better, but make sure each step has sufficient details to accomplish it. Do not actually perform the task, just list the steps.

<task>
{user_task}
</task>
'''

    @classmethod
    def action_prompt(cls, current_action: str):
        return f'''Perform the following action. Keep the following behaviors in mind when performing these actions:
1. <behavior>If you open a new window or view or subview and you don't see what you expect then exit out of it or go back to the previous part you were just in.</behavior>
2. <behavior>For whatever action you try, you may try at most two times. If what you are trying to do doesn't work by the second time then stop, and tell us why this didn't work.</behavior>

<action>{current_action}</action>
'''

    @classmethod
    def critique_prompt(cls, current_action: str, next_action: str):
        return f'''
Self critique your work so far, did you complete the action below and are you at the expected end state?

<action>{current_action}</action>

Finish self-critiquing by asking yourself if you're ready to perform this next action:

<action>{next_action}</action>
'''

    @classmethod
    def final_critique_prompt(cls, current_action: str, next_action: str):
        return f'''
Self critique your work so far, did you complete the action below and are you at the expected end state?

<action>{current_action}</action>

Finish self-critiquing by asking yourself if you're ready to perform this next action:

<action>{next_action}</action>
'''


if __name__ == '__main__':
    out = COT_PROMPTS.planning_prompt(user_task="Hello world!")
    print(out)
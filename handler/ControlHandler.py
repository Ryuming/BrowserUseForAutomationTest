from browser_use import Controller, ActionResult


@controller.action('Complete survey with answers got from asking user')
def complete_surrvey_by_asking_user(question: str) -> ActionResult:
    answer = input(f'{question}>')
    return ActionResult(extracted_content= f'The human responded with: {answer}', included_in_memory=True)
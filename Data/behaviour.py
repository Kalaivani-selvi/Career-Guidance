import pandas as pd
import random

# Define the questions, options, and correct answers
questions = [
    "You're leading a team project, and a member proposes an unconventional approach. What do you do?",
    "Your project is facing a sudden roadblock due to unforeseen circumstances. What is your immediate action?",
    "You have two equally qualified candidates for a position. How do you decide whom to hire?",
    "You're tasked with completing multiple assignments with tight deadlines. How do you prioritize?",
    "Your team is suddenly assigned to a project in a completely different industry. How do you approach this change?",
    " Your marketing campaign isn't achieving the expected results. How do you analyze the situation?",
    "A key team member unexpectedly quits midway through a project. What steps do you take to mitigate the impact?",
    "Your team is divided on a crucial decision. How do you facilitate consensus?",
    "You're assigned multiple tasks but lack sufficient time to complete them all. What do you do?",
    "You're given a new software tool to use for your daily tasks. How do you approach learning and integrating it into your workflow?",
    "You're presented with conflicting data regarding a project's performance. How do you determine the most accurate information?",
    "Your team encounters a technical issue that halts progress. What steps do you take to troubleshoot?",
    " You're tasked with choosing between two vendors for a critical project component. How do you make your selection?",
    "You're juggling multiple deadlines and feel overwhelmed. How do you regain control of your schedule?",
    "Your team undergoes a significant restructuring. How do you adjust to the new dynamics?",
    "Your project plan encounters unforeseen obstacles. How do you modify your approach?",
    "A key stakeholder disagrees with the proposed solution to a project issue. How do you handle the disagreement?",
    "Your team is divided on whether to pursue a risky but potentially lucrative opportunity. How do you proceed?",
    " You're responsible for organizing a large event with a tight deadline. How do you ensure everything gets done on time?",
    "Your company adopts a new project management methodology. How do you adapt your working style?",
    "Your project team encounters unexpected challenges. How do you encourage innovative solutions?",
    "A customer is dissatisfied with a product. How do you address their concerns?",
    "Your team is split on whether to invest in new technology. How do you reach a decision?",
    "You have multiple tasks due today, but unexpected urgent work arises. How do you manage your time effectively?",
    "Your company undergoes a major restructuring, resulting in changes to your role. How do you adapt to the new responsibilities?",
    "Your team proposes a solution to a problem, but you foresee potential negative consequences. What is your response?",
    "A project deadline is at risk due to unforeseen circumstances. How do you ensure timely completion?",
    "Your team needs to choose between two software solutions. How do you make the decision?",
    "You have a long-term project with multiple milestones. How do you ensure steady progress?",
    "Your team's goals change abruptly. How do you adjust your priorities?",
    "Your team's proposed solution to a problem requires a significant investment. How do you evaluate its potential success?",
    "A key resource for your project suddenly becomes unavailable. How do you adapt to the situation?",
    "Your team is divided on whether to pursue a new market opportunity. How do you facilitate consensus?",
    "You have multiple urgent tasks to complete. How do you prioritize them?",
    "Your project scope changes midway through execution. How do you adjust your approach?",
    "Your team is presented with conflicting data regarding a market trend. How do you determine the most accurate information?",
    "A project stakeholder proposes a solution that conflicts with the project objectives. How do you address the situation?",
    "Your team needs to select a vendor for an essential project component. How do you make the decision?",
    "You're responsible for organizing a team meeting with stakeholders in different time zones. How do you coordinate the meeting effectively?",
    "Your company implements a new software system for project management. How do you adapt to the change?",
    "Your team is brainstorming ideas for a new marketing campaign. How do you ensure that all perspectives are considered?",
    "A project you're leading encounters unexpected budget constraints. How do you address this issue?",
    "Your team is debating between two software platforms for project management. How do you make the final decision?",
    "You have multiple deadlines approaching simultaneously. How do you prioritize your tasks?",
    "Your team's project scope changes significantly. How do you ensure that everyone is aligned with the new objectives?",
    "Your company is considering expanding into a new market. How do you evaluate the potential risks and opportunities?",
    "A project deadline is approaching, but your team encounters unexpected technical issues. How do you address this challenge?",
    "Your team needs to choose a strategy for entering a competitive market. How do you make this decision?",
    "You have a long-term project with multiple phases. How do you ensure that each phase stays on schedule?",
    "Your company implements a new organizational structure. How do you adapt to changes in reporting lines and responsibilities?"
    
]

options = [
    ["Dismiss the idea and stick to the original plan.","Immediately implement the new approach without further analysis.","Encourage discussion to understand the potential benefits and drawbacks.","Assign the team member a different task to avoid disruption."],
    ["Panic and escalate the issue to higher management","Ignore the problem and hope it resolves itself.","Gather the team to assess the situation and brainstorm potential solutions.","Blame others for the setback and seek retribution."],
    ["Choose the candidate with the higher salary expectation.","Select the candidate who shares the most personal interests with you.","Base your decision on their relevant skills and experience for the role.","Randomly pick one to avoid bias."],
    ["Work on tasks as they come in, regardless of deadline urgency.","Focus solely on tasks that seem easiest to complete first.","Prioritize tasks based on deadlines and importance, tackling the most critical ones first.","Delegate all tasks to other team members to alleviate pressure."],
    ["Refuse to work on the project as it's outside your expertise.","Research and learn about the new industry to understand its dynamics.","Immediately request to be transferred to a different team","Ignore the project until more information is provided."],
    ["Assume the target audience isn't interested and abandon the campaign.","Review the campaign data to identify patterns and potential areas for improvement.","Blame external factors for the campaign's failure."," Increase the advertising budget without further analysis."],
    ["Delay the project until a replacement is found.","Divide the work among remaining team members and work overtime to compensate.","Assess the remaining team's skills and redistribute tasks accordingly."," Cancel the project due to lack of resources."],
    ["Dictate the decision based on your own judgment.","Avoid confrontation by postponing the decision indefinitely.","Encourage open discussion and seek common ground among team members.","Side with the majority opinion regardless of its merit."],
    ["Sacrifice quality to meet deadlines.","Prioritize tasks based on urgency and negotiate deadlines for less critical ones.","Inform management that the workload is unmanageable and request assistance.","Ignore less urgent tasks until they become critical."],
    ["Ignore the new tool and continue with existing methods.","Resist the change and express frustration to management.","Embrace the opportunity to learn and adapt, seeking training if necessary.","Delegate the task of learning the new tool to a colleague."],
    ["Disregard the data and rely on intuition.","Consult with colleagues to gather additional perspectives.","Accept the data provided without further scrutiny.","Immediately report the discrepancy to upper management."],
    ["Panic and escalate the issue to IT support.","Attempt random solutions until the problem is resolved.","Analyze the problem systematically and research potential solutions.","Ignore the issue and hope it resolves itself."],
    ["Pick the vendor with the lowest cost, regardless of quality.","Base your decision on personal preferences or past experiences.","Evaluate both vendors objectively, considering factors such as reliability and track record.","Delegate the decision to a colleague to avoid responsibility."],
    ["Work longer hours to catch up on tasks.","Prioritize tasks and create a detailed schedule to manage time effectively.","Ignore non-urgent tasks until they become critical.","Delegate all tasks to avoid personal stress."],
    ["Resist change and express dissatisfaction openly.","Seek opportunities to learn new skills and adapt to the new environment.","Ignore the restructuring and continue with existing workflows.","Immediately start looking for a new job outside the company."],
    ["Stick to the original plan and hope for the best outcome.","Abandon the project entirely due to difficulties.","Analyze the obstacles and adjust the plan accordingly.","Blame external factors for the project's failure."],
    ["Ignore the stakeholder's concerns and proceed with the solution.", "Convince the stakeholder that your solution is the only viable option.","Listen to the stakeholder's feedback and collaborate to find a mutually acceptable solution.","Escalate the disagreement to upper management for resolution."],
    ["Reject the opportunity to avoid potential failure.","Proceed with the opportunity without consulting the team.","Evaluate the risks and benefits collaboratively with the team before making a decision.","Flip a coin to decide whether to pursue the opportunity."],
    ["Procrastinate and hope for the best outcome.","Break down tasks into manageable chunks and create a timeline for completion.","Delegate all tasks to others and take a hands-off approach.","Ignore the deadline and focus on other priorities."],
    [ "Resist the change and continue with familiar methods.","Embrace the new methodology and seek training to become proficient.","Ignore the new methodology and work independently.","Criticize the new methodology openly to colleagues."],
    ["Discourage any deviations from the original plan to maintain consistency.","Implement solutions that have worked in the past for similar challenges.","Foster an environment where team members are encouraged to think creatively and suggest new ideas.","Assign blame for the challenges and focus on finding someone to hold "],
    ["Dismiss the customer's feedback as unwarranted.","Offer a refund without investigating the issue further.","Listen to the customer's concerns, investigate the problem, and propose appropriate solutions.","Ignore the complaint and hope the customer forgets about it."],
    ["Follow the recommendation of the team member with the most experience.","Make a quick decision without considering all available information.","Gather data, analyze potential benefits and risks, and involve the team in the decision-making process.","Delay the decision indefinitely to avoid conflict."],
    ["Ignore the urgent work and focus on completing tasks with earlier deadlines.","Prioritize the urgent work and adjust your schedule accordingly to meet the new deadline.","Delegate all tasks to colleagues and take the day off.","Panic and attempt to complete all tasks simultaneously."],
    ["Resist the changes and insist on maintaining your previous role.","Embrace the opportunity to learn new skills and adapt to the new role.","Immediately start looking for a new job outside the company.","Ignore the changes and continue with your old responsibilities."],
    ["Accept the solution without further consideration.","Dismiss the concerns and proceed with the proposed solution.","Voice your concerns and collaborate with the team to find a better solution.","Ignore the proposed solution and come up with your own alternative."],
    ["Extend the deadline without consulting stakeholders.","Panic and assign blame for the delay.","Assess the situation, adjust the project plan if necessary, and communicate with stakeholders about the new timeline.","Ignore the issue and hope it resolves itself."],
    ["Select the cheaper option to save costs.","Base the decision solely on personal preference.","Evaluate both options based on features, compatibility, and long-term benefits.","Ask someone outside the team to make the decision for you."],
    ["Procrastinate and rush to complete the project just before the deadline.","Break down the project into smaller tasks and set deadlines for each milestone.","Ignore the project until the deadline approaches.","Delegate the entire project to someone else and take credit for their work."],
    [ "Resist the changes and continue pursuing the previous goals."," Immediately abandon the old goals and fully commit to the new ones.","Evaluate the new goals and adjust your priorities accordingly.","Ignore the changes and continue with your existing priorities."],
    ["Trust the team's judgment and proceed with the investment.","Conduct thorough research and analysis to assess the solution's viability.","Reject the solution without further consideration.","Consult with external experts to make the decision."],
    ["Panic and halt the project until the resource becomes available again.","Identify alternative resources and adjust the project plan accordingly.","Continue with the project as planned and hope for the best.","Blame the resource for the setback and seek disciplinary action."],
    ["Side with the majority opinion to avoid conflict.","Delegate the decision-making responsibility to someone else.","Encourage open discussion and seek common ground among team members.","Reject the opportunity to avoid potential risks."],
    ["Work on tasks randomly as they come to mind.","Prioritize tasks based on their impact on project deadlines and goals.","Focus only on tasks that are personally interesting to you.","Delegate all tasks to others to alleviate pressure."],
    ["Ignore the changes and continue with the original plan.","Resist the changes and insist on sticking to the initial scope.","Embrace the changes and modify the project plan accordingly.","Blame others for the changes and refuse to cooperate."],
    ["Base decisions on intuition rather than data.","Disregard the conflicting data and proceed with existing assumptions.","Analyze the sources of the data and assess their credibility.","Consult with competitors to verify the accuracy of the data."],
    ["Accept the stakeholder's solution without question.","Reject the stakeholder's solution without explanation.", "Engage in open dialogue to understand the stakeholder's perspective and find a compromise.","Ignore the stakeholder's input and proceed with the original plan."],
    ["Choose the vendor with the lowest price to save costs.","Base the decision solely on your personal preference.","Evaluate vendors based on factors such as reputation, reliability, and past performance.","Delegate the decision to a colleague to avoid responsibility."],
    ["Schedule the meeting at a time convenient for you, regardless of others' availability.", "Conduct multiple separate meetings to accommodate different time zones.","Use scheduling tools to find a suitable time that works for all participants.","Cancel the meeting due to scheduling difficulties."],
    ["Ignore the new system and continue using existing methods.","Resist the change and express frustration to management.","Embrace the new system and seek training to become proficient.","Refuse to use the new system and insist on using alternative tools."],
    ["Only consider ideas from senior team members.","Limit the brainstorming session to avoid too many ideas.","Encourage all team members to contribute ideas and actively listen to each suggestion.","Reject any ideas that deviate from the traditional marketing approach."],
    ["Increase the project's budget without consulting stakeholders.","Cut corners to meet the original budget.","Analyze the project's scope and requirements to identify areas where costs can be reduced.","Ignore the budget constraints and continue as planned."],
    ["Choose the platform with the most features, regardless of cost.","Select the platform that is easiest to implement, even if it lacks certain features.","Evaluate both platforms based on cost, features, user-friendliness, and scalability.","Let individual team members choose which platform they prefer."],
    ["Work on tasks in the order they were assigned.","Prioritize tasks based on their urgency and importance.","Focus only on tasks that are personally enjoyable.","Delegate all tasks to others to alleviate the workload.",],
    ["Assume that everyone will adapt without any communication.","Hold a team meeting to discuss the changes and clarify expectations.","Ignore the changes and continue with the original project plan.","Blame the project manager for the changes and refuse to cooperate."],
    ["Base the decision solely on intuition.","Conduct thorough market research and analysis to assess the viability of expansion.","Ignore potential risks and focus only on potential opportunities.","Delegate the decision to someone else to avoid responsibility."],
    ["Extend the deadline without consulting stakeholders.","Blame the technical team for the issues and demand immediate resolution.","Collaborate with the technical team to identify and resolve the issues as quickly as possible.","Ignore the technical issues and hope they resolve themselves."],
    ["Adopt the same strategy as your competitors to minimize risk.","Conduct a SWOT analysis to evaluate different strategic options.","Choose the strategy that promises the highest potential return on investment.","Let individual team members decide which strategy they prefer."],
    ["Delay the start of each phase to accommodate unforeseen delays.","Set strict deadlines for each phase and closely monitor progress.","Ignore project milestones and focus only on the final deadline.","Delegate responsibility for managing individual phases to team members."],
    ["Resist the changes and insist on maintaining your previous reporting structure.","Embrace the new structure and seek clarification on your role and responsibilities.","Ignore the changes and continue with your previous reporting lines.","Blame management for the changes and refuse to cooperate."]
  
    
    
  
]

correct_answers =  ['c','c','c','c','b','b','c','c','b','c','b','c','c','b','b','c','c','c','b','b','c','c','c','b','b','c','c','c','b','c','b','b','c','b','c','c','c','c','c','c','c','c','c','b','b','b','c','b','b','b']

# Check lengths
print("Number of questions:", len(questions))
print("Number of options lists:", len(options))
print("Number of correct answers:", len(correct_answers))

# Find problematic question
for i, (question, option) in enumerate(zip(questions, options)):
    if len(option) != 4:
        print("Question", i+1, "has an issue. Number of options:", len(option))

# Generate synthetic dataset
data = {"Question": questions, "Option A": [], "Option B": [], "Option C": [], "Option D": [], "Correct Answer": []}

for options_list, correct_answer in zip(options, correct_answers):
    # random.shuffle(options_list)  # Remove this line to avoid shuffling options
    data["Option A"].append(options_list[0])
    data["Option B"].append(options_list[1])
    data["Option C"].append(options_list[2])
    data["Option D"].append(options_list[3])
    data["Correct Answer"].append(correct_answer)

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the synthetic dataset
print(df)

# Save to CSV file
df.to_csv("round2.csv", index=False)
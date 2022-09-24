from formulation.formulation import *

def read_dataset(filename):
  
  f = open("input/" + filename + ".txt", 'r')
  line = f.readline()
  tokens = line.split()
  team = Team(int(tokens.pop(0)), int(tokens.pop(0)))

  #For each member read: member_name member_skills_no
  for i in range(team.n_members):
    #
    line = f.readline()
    tokens = line.split()
    member = Member(tokens.pop(0))
    
    #For each skill read: skill_name skill_level
    for k in range(int(tokens.pop(0))):
      line = f.readline()
      tokens = line.split()
      skill = Skill(tokens.pop(0), int(tokens.pop(0)))
      member.skills.append(skill)
      
    team.members.append(member)

  for i in range(team.n_projects):
    line = f.readline()
    tokens = line.split()
    trash = tokens.pop(3)
    
    project = Project(tokens.pop(0), int(tokens.pop(0)), int(tokens.pop(0)), int(tokens.pop(0)))

    for k in range (project.n_roles):
      line = f.readline()
      tokens = line.split()
      role = Skill(tokens.pop(0), int(tokens.pop(0)))
      project.roles.append(role)

    team.projects.append(project)

  return team

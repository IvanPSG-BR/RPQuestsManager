from datetime import datetime, time

class Quest:
    def __init__(self, description, time_str, time, difficulty, priority, status):
        self.description = description
        self.time_str = time_str
        self.time = time
        self.difficulty = difficulty
        self.priority = priority
        self.status = status
        self.quests = []

    def create_quest(self):
        while True:
            description = input("Insira a missão: ")
            time_str = input("Informe o horário da missão [HH:MM]: ")
            time = datetime.strptime(time_str, "%H:%M")
            difficulty = input("Informe a dificuldade [1-3]: ")
            priority = input("Informe a prioridade [1-3]: ")
            status = "Pendente"
            quest = Quest(description, time_str, time, difficulty, priority, status)
            self.quests.append(quest)

            add_more = input("Deseja adicionar mais uma missão? [S/N]: ").upper().strip()
            if "N" in add_more:
                break

        return self.quests
    
    def show_quests(self, specific_quest):
        for indice, q in enumerate(specific_quest, start=1):
            status_marker = ("[X]" if q.status == "Concluída" else "[ ]")
            print(f"{indice}: {status_marker} {q.description}\nHorário: {q.time_str}\nDificuldade: {q.difficulty}\nPrioridade: {q.priority}\nStatus: {q.status}\n")
            print("\n")
    
    def complete_quest(self):
        choice_quest = int(input("Informe qual missão deseja marcar como concluída: ")) - 1
        self.quests[choice_quest].status = "Concluída"
        print(f"Missão '{self.quests[choice_quest].description}' concluída!")
        
        self.completed_quests = [q for q in self.quests if q.status == "Concluída"]
        self.pendant_quests = [q for q in self.quests if q.status != "Concluída"]

    def update_quest(self):
        choice_quest = int(input("Informe qual missão deseja atualizar: "))
        self.quests[choice_quest].description = input("Informe a nova missão: ")
        time_str = input("Informe o horário da missão [HH:MM]: ")
        self.quests[choice_quest].time = datetime.strptime(time_str, "%H:%M")
        self.quests[choice_quest].difficulty = input("Informe a dificuldade [1-3]: ")
        self.quests[choice_quest].priority = input("Informe a prioridade [1-3]: ")
        print(f"Missão '{self.quests[choice_quest].description}' atualizada!")
            
    def delete_quest(self):
        choice_quest = int(input("Informe qual missão deseja deletar: ")) - 1
        quest_description = self.quests[choice_quest].description
        del self.quests[choice_quest]
        print(f"Missão '{quest_description}' deletada!")

class User:
    def __init__(self, username, experience, level, honor, coins, achievements, rewards, max_exp):
        self.username = username
        self.experience = experience
        self.level = level
        self.honor = honor
        self.coins = coins
        self.achievements = achievements
        self.rewards = rewards
        self.max_exp = max_exp
        self.user = {}
        self.quest_manager = Quest()

    def create_user(self):
        username = input("Nome do usuário: ")
        experience = 0
        level = 1
        honor = 0
        coins = 0
        achievements = []
        rewards = []
        max_exp = 100
        users = User(username, experience, level, honor, max_exp, coins, achievements, rewards)
        self.user[username] = users

        return self.user
    
    def show_user_info(self):
        for info in self.user:
            print(f"Nome do usuário: {info.username}")
            print(f"Nível: {info.level}")
            print(f"Experiência: {info.experience}")
            print(f"Reputação: {info.honor}")
            print(f"Exp restante para próximo nível: {info.max_exp - info.experience}")
            print(f"Moedas: {info.coins}")
            print(f"Conquistas: {info.achievements} - {info.rewards}")

    def change_username(self):
        choice_user = int(input("Informe o usuário que deseja alterar o nome: ")) - 1
        new_username = input("Informe o novo nome do usuário: ")
        self.user[choice_user].username = new_username
        print(f"Nome do usuário '{self.user[choice_user].username}' alterado para '{new_username}'!")

    def exp_multiplier(self):
        multipliers_lvl = {"reputação": 1/100,
                           "dificuldade": [5/100, 10/100, 15/100],
                           "prioridade": [3/100, 5/100, 10/100]}
        for q in self.quest_manager.quests:
            if self.quest_manager.quests[q].status == "Concluída":
                if self.quest_manager.quests[q].time > datetime.now():
                    self.user[self.username].honor += 5
                elif self.quest_manager.quests[q].time < datetime.now():
                    self.user[self.username].honor -= 5
                else:
                    pass
        honor_bonus = self.user[self.username].honor + (self.user[self.username].honor * multipliers_lvl["reputação"])
        difficulty_bonus = self.user[self.username].honor + (self.user[self.username].honor * multipliers_lvl["dificuldade"][self.quest_manager.quests[q].difficulty - 1])
        priority_bonus = self.user[self.username].honor + (self.user[self.username].honor * multipliers_lvl["prioridade"][self.quest_manager.quests[q].priority - 1])
        total_multiplier = honor_bonus + difficulty_bonus + priority_bonus
        return total_multiplier

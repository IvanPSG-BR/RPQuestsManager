class Quest:
    def __init__(self, description, time, difficulty, priority, status):
        self.description = description
        self.time = time
        self.difficulty = difficulty
        self.priority = priority
        self.status = status
        self.quests = []

    def create_quest(self):
        while True:
            description = input("Insira a missão: ")
            time = input("Informe o horário da missão [HH:MM]: ")
            difficulty = input("Informe a dificuldade [1-3]: ")
            priority = input("Informe a prioridade [1-3]: ")
            status = "Pendente"
            quest = Quest(description, time, difficulty, priority, status)
            self.quests.append(quest)

            add_more = input("Deseja adicionar mais uma missão? [S/N]: ").upper().strip()
            if "N" in add_more:
                break

        return self.quests

    def show_quests(self, specific_quest):
        for indice, q in enumerate(specific_quest, start=1):
            status_marker = ("[X]" if q.status == "Concluída" else "[ ]")
            print(f"""{indice}: {status_marker} {q.description}\n
                  Horário: {q.time}\n
                  Dificuldade: {q.difficulty}\n
                  Prioridade: {q.priority}\n
                  Status: {q.status}\n""")
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
        self.quests[choice_quest].time = input("Informe o horário da missão [HH:MM]: ")
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
        self.user = []
        self.quest_manager = Quest()

    def create_user(self):
        username = input("Nome do usuário: ")
        experience = 0
        level = 1
        honor = 0
        coins = 0
        achievements = []
        rewards = {}
        max_exp = 100
        users = User(username, experience, level, honor, max_exp, coins, achievements, rewards)
        self.user.append(users)

        return self.user

    def show_user_info(self):
        desc = ["Nome do usuário: ", 
                "Experiência: ", 
                "Nível: ", 
                "Reputação: ", 
                "Exp restante para próximo nível: ", 
                "Moedas: ", 
                "Conquistas: ", 
                "Recompensas: "]
        for info in self.user:
            print(desc[info], info if info != self.user.max_exp else desc[info], (info - self.user.experience))

    def change_username(self):
        choice_user = int(input("Informe o usuário que deseja alterar o nome: ")) - 1
        new_username = input("Informe o novo nome do usuário: ")
        self.user[choice_user].username = new_username
        print(f"Nome do usuário '{self.user[choice_user].username}' alterado para '{new_username}'!")

    def gain_exp(self):
        

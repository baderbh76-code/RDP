# إدارة الموجهات (Prompts) والقيود (Restrictions) وإعداد النظام (System Configuration) في هذا الملف.

class PromptManager:
    def __init__(self):
        self.prompts = []  # قائمة لتخزين الموجهات
        self.restrictions = []  # قائمة لتخزين القيود
        self.system_config = {}  # إعدادات النظام

    def add_prompt(self, prompt):
        # إضافة موجه جديد
        self.prompts.append(prompt)

    def remove_prompt(self, prompt):
        # إزالة ��وجه
        if prompt in self.prompts:
            self.prompts.remove(prompt)

    def add_restriction(self, restriction):
        # إضافة قيد جديد
        self.restrictions.append(restriction)

    def remove_restriction(self, restriction):
        # إزالة قيد
        if restriction in self.restrictions:
            self.restrictions.remove(restriction)

    def set_system_config(self, key, value):
        # إعداد تكوين النظام
        self.system_config[key] = value

    def get_system_config(self):
        # الحصول على إعدادات النظام
        return self.system_config

# مثال على كيفية استخدام الفئة
if __name__ == '__main__':
    manager = PromptManager()
    manager.add_prompt('موجه 1')
    manager.add_restriction('قيد 1')
    manager.set_system_config('اللغة', 'العربية')
    print(manager.get_system_config())
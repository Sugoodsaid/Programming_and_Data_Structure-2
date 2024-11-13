import tkinter as tk
from tkinter import simpledialog, messagebox
import json

class ShoppingList:
    def __init__(self):
        self.items = []
        
        ShoppingList = self.items 

    def add_item(self, item):
        """إضافة عنصر إلى لستة التسوق"""
        self.items.append(item)
        messagebox.showinfo("Success", f'Added: {item}')

    def delete_item(self, item):
        """مسح عنصر من لستة التسوق"""
        try:
            self.items.remove(item)
            messagebox.showinfo("Success", f'Deleted: {item}')
        except ValueError:
            messagebox.showerror("Error", f'Item not found: {item}')

    def modify_item(self, old_item, new_item):
        """تعيين و تبديل عنصر من لستة التسوق"""
        try:
            index = self.items.index(old_item)
            self.items[index] = new_item
            messagebox.showinfo("Success", f'Modified: {old_item} to {new_item}')
        except ValueError:
            messagebox.showerror("Error", f'Item not found: {old_item}')

    def display_items(self):
        """عرض جميع عناصر لستة التسوق"""
        if not self.items:
            messagebox.showinfo("Shopping List", "Shopping list is empty.")
        else:
            items_str = "\n".join(self.items)
            messagebox.showinfo("Shopping List", f"Items:\n{items_str}")

    def save_to_file(self, filename):
        """ حفظ لستة التسوق في الملف"""
        with open(filename, 'w') as file:
            json.dump(self.items, file)
        messagebox.showinfo("Success", f'Saved shopping list to {filename}')

    def load_from_file(self, filename):
        """تحميل لستة التسوق من الملف"""
        try:
            with open(filename, 'r') as file:
                self.items = json.load(file)
            messagebox.showinfo("Success", f'Loaded shopping list from {filename}')
        except FileNotFoundError:
            messagebox.showerror("Error", f'File not found: {filename}')
        except json.JSONDecodeError:
            messagebox.showerror("Error", f'Error decoding JSON from the file: {filename}')

class ShoppingListApp:
    def __init__(self, root):
        self.shopping_list = ShoppingList()
        self.root = root
        self.root.title("Shopping List Application")

        # إنشاء إطار لتجميع الأزرار
        frame = tk.Frame(root)
        frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # قائمة الخيارات
        options = [
            "Add Item", "Delete Item", "Modify Item",
            "Display Items", "Save to File", "Load from File",
            "Exit"
        ]
        # إنشاء الأزرار مع حدود في ثلاث أسطر
        for index, option in enumerate(options):
        	button = tk.Button(frame, text=option, borderwidth=2, relief="solid", command=lambda opt=option: self.handle_option(opt))
        	button.grid(row=index // 3, column=index % 3, padx=5, pady=5, sticky="nsew")

        # إنشاء الأزرار مع حدود في ثلاث أسطر
        for index, option in enumerate(options):
            button = tk.Button(frame, text=option, borderwidth=2, relief="solid", command=lambda opt=option: self.handle_option(opt))
            button.grid(row=index // 3, column=index % 3, padx=5, pady=5, sticky="nsew")

        # ضبط وزن الأعمدة والصفوف
        for i in range(3):
            frame.grid_columnconfigure(i, weight=1)
        for i in range(3):
            frame.grid_rowconfigure(i, weight=1)

    def handle_option(self, option):
        if option == "Add Item":
            item = simpledialog.askstring("Input", "Enter item to add:")
            if item:
                self.shopping_list.add_item(item)
        elif option == "Delete Item":
            item = simpledialog.askstring("Input", "Enter item to delete:")
            if item:
                self.shopping_list.delete_item(item)
        elif option == "Modify Item":
            old_item = simpledialog.askstring("Input", "Enter item to modify:")
            if old_item:
                new_item = simpledialog.askstring("Input", "Enter new item:")
                if new_item:
                    self.shopping_list.modify_item(old_item, new_item)
        elif option == "Display Items":
            self.shopping_list.display_items()
        elif option == "Save to File":
            filename = simpledialog.askstring("Input", "Enter filename to save:")
            if filename:
                self.shopping_list.save_to_file(filename)
        elif option == "Load from File":
            filename = simpledialog.askstring("Input", "Enter filename to load:")
            if filename:
                self.shopping_list.load_from_file(filename)
        elif option == "Exit":
            	self.root.quit()
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1300x600")  # تعيين حجم النافذة الابتدائي
    app = ShoppingListApp(root)
    root.mainloop()

class Editor:
    def view_documnet(self):
        print("Document is oppened for the view")
    def edit_documnet(self):
        print("Editing document possible only in PRO version")
class ProEditor(Editor):
    def edit_documnet(self):
        print("Document edits")

def main():
    print('Welcome to Editor!')
    while(True):
        print(
"""
Choose action:
1.View Documnet
2.Edit Document
3.Exit          
""")
        action = input()
        editor = Editor()
        print(id(editor))
        if action == '1':
            editor.view_documnet()
        elif action == '2':
            editor.view_documnet()
            license_key = input("Enter the licence key for PRO version: ")
            if license_key == "2174516":
                proEdit = ProEditor()
                proEdit.edit_documnet()
            else:
                print("Wrong licence key!")
                Editor.view_documnet()
        elif action == '3':
            print("Bye Bye!")
            break
            
if __name__ == '__main__':
    main()
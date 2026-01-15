# Goal: Create @admin_required. If global USER!= 'admin', raise PermissionError.

# Deep Dive: The decorator acts as a gatekeeper. It excutes before the sensitive function is entered.
#            If the check fails, the stack frame for the target function is never even created.

USER="admin"

def admin_required(func):
    # global USER
    def wrap():
        if USER!="admin":
            raise PermissionError
        return func()
    return wrap

@admin_required
def dashboard():
    print(f"Admin panel")

dashboard()
        
        
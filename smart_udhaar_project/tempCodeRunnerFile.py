import customtkinter as ctk
from tkinter import messagebox, ttk
from db_config import connect_db

# --- GLOBAL THEME SETTINGS ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SmartUdhaarApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Udhaar v4.0 - Enterprise Ledger")
        self.geometry("1300x800")
        
        # Configure Table Text Size Globally
        self.setup_table_style()
        
        # Start at Login
        self.show_login()

    def setup_table_style(self):
        """Increases the font size for all tables in the app"""
        style = ttk.Style()
        style.theme_use("default")
        
        # Configure Treeview (Data rows) font size
        style.configure("Treeview", 
                        background="#2a2d2e", 
                        foreground="white", 
                        rowheight=35, # Increased row height for bigger text
                        fieldbackground="#2a2d2e",
                        font=("Arial", 13)) # Increased font size to 13
        
        # Configure Headings font size
        style.configure("Treeview.Heading", 
                        font=("Arial", 14, "bold"), # Increased heading size to 14
                        background="#1f1f1f", 
                        foreground="white")
        
        style.map("Treeview", background=[('selected', '#1f538d')])

    # --- 1. LOGIN SCREEN ---
    def show_login(self):
        for widget in self.winfo_children(): widget.destroy()
        self.login_bg = ctk.CTkFrame(self, fg_color="transparent")
        self.login_bg.pack(expand=True, fill="both")

        self.login_card = ctk.CTkFrame(self.login_bg, width=500, height=650, corner_radius=35, border_width=2)
        self.login_card.place(relx=0.5, rely=0.5, anchor="center")
        self.login_card.pack_propagate(False)

        ctk.CTkLabel(self.login_card, text="💳", font=("Arial", 80)).pack(pady=(70, 10))
        ctk.CTkLabel(self.login_card, text="SMART UDHAAR", font=("Century Gothic", 32, "bold")).pack(pady=5)
        ctk.CTkLabel(self.login_card, text="Complete Inventory & Ledger System", font=("Arial", 14), text_color="gray").pack(pady=(0, 50))

        self.user_entry = ctk.CTkEntry(self.login_card, placeholder_text="Username", width=340, height=55, corner_radius=15)
        self.user_entry.pack(pady=12, padx=70)
        self.pass_entry = ctk.CTkEntry(self.login_card, placeholder_text="Password", show="*", width=340, height=55, corner_radius=15)
        self.pass_entry.pack(pady=12, padx=70)

        ctk.CTkButton(self.login_card, text="SECURE LOGIN", command=self.handle_login, width=340, height=60, corner_radius=15, font=("Arial", 18, "bold")).pack(pady=(45, 20))

    def handle_login(self):
        if self.user_entry.get() == "admin" and self.pass_entry.get() == "admin123":
            self.show_dashboard()
        else:
            messagebox.showerror("Auth Error", "Invalid Username or Password.")

    # --- 2. MAIN NAVIGATION ---
    def show_dashboard(self):
        for widget in self.winfo_children(): widget.destroy()
        self.sidebar = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color="#121212")
        self.sidebar.pack(side="left", fill="y")
        
        ctk.CTkLabel(self.sidebar, text="💳 SMART UDHAAR", font=("Century Gothic", 22, "bold")).pack(pady=40)
        
        self.create_nav_btn("  🏠   Home Overview", self.draw_home)
        self.create_nav_btn("  👤   Add Customer", self.draw_add_customer)
        self.create_nav_btn("  📋   Full Directory", self.draw_customer_directory)
        self.create_nav_btn("  🛒   Udhaar Item Tracking", self.draw_item_tracking)
        self.create_nav_btn("  📊   Credit Analysis", self.draw_customer_logs)

        ctk.CTkButton(self.sidebar, text="LOGOUT", fg_color="#551a1a", hover_color="#882222", height=45, corner_radius=12, command=self.show_login).pack(side="bottom", pady=30, padx=30, fill="x")

        self.main_view = ctk.CTkFrame(self, corner_radius=30, fg_color="#181818")
        self.main_view.pack(side="right", fill="both", expand=True, padx=30, pady=30)
        self.draw_home()

    def create_nav_btn(self, text, command):
        btn = ctk.CTkButton(self.sidebar, text=text, anchor="w", height=50, fg_color="transparent", hover_color="#2b2b2b", font=("Arial", 14), command=command)
        btn.pack(pady=5, padx=20, fill="x")

    # --- 3. PAGE: HOME OVERVIEW ---
    def draw_home(self):
        for widget in self.main_view.winfo_children(): widget.destroy()
        header = ctk.CTkFrame(self.main_view, fg_color="transparent")
        header.pack(fill="x", padx=60, pady=(40, 20))
        ctk.CTkLabel(header, text="System Statistics", font=("Century Gothic", 36, "bold")).pack(side="left")
        
        center_frame = ctk.CTkFrame(self.main_view, fg_color="transparent")
        center_frame.pack(expand=True, fill="both", padx=40)

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(total_udhaar), COUNT(*) FROM customers")
        stats = cursor.fetchone()
        cursor.execute("SELECT COUNT(*) FROM products")
        total_prods = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM credit_scores WHERE score < 40")
        blacklisted = cursor.fetchone()[0]
        conn.close()

        self.create_stat_card(center_frame, "Market Debt", f"Rs. {stats[0] or 0}", "#1a3a5f", 0)
        self.create_stat_card(center_frame, "Inventory Items", str(total_prods), "#2a2a2a", 1)
        self.create_stat_card(center_frame, "Risk Customers", str(blacklisted), "#5a1a1a", 2)

    def create_stat_card(self, parent, title, value, color, col):
        card = ctk.CTkFrame(parent, width=320, height=180, fg_color=color, corner_radius=25)
        card.grid(row=0, column=col, padx=20, pady=20)
        card.grid_propagate(False)
        ctk.CTkLabel(card, text=title, font=("Arial", 16, "bold")).pack(pady=(45, 10))
        ctk.CTkLabel(card, text=value, font=("Arial", 38, "bold")).pack()

    # --- 4. PAGE: UDHAAR ITEM TRACKING ---
    def draw_item_tracking(self):
        for widget in self.main_view.winfo_children(): widget.destroy()
        ctk.CTkLabel(self.main_view, text="Detailed Udhaar Purchases", font=("Century Gothic", 30, "bold")).pack(pady=30, padx=60, anchor="w")
        
        table_container = ctk.CTkFrame(self.main_view, fg_color="transparent")
        table_container.pack(fill="both", expand=True, padx=60, pady=10)
        
        cols = ("Customer", "Item Name", "Qty", "Price", "Subtotal", "Date")
        tree = ttk.Treeview(table_container, columns=cols, show='headings')
        
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor="center")

        tree.pack(side="left", fill="both", expand=True)
        
        conn = connect_db()
        cursor = conn.cursor()
        query = """
            SELECT c.full_name, p.name, ti.quantity, ti.unit_price, ti.subtotal, t.transaction_date
            FROM customers c
            JOIN transactions t ON c.customer_id = t.customer_id
            JOIN transaction_items ti ON t.transaction_id = ti.transaction_id
            JOIN products p ON ti.product_id = p.product_id
            WHERE t.type = 'udhaar'
            ORDER BY t.transaction_date DESC
        """
        cursor.execute(query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

    # --- 5. PAGE: DIRECTORY ---
    def draw_customer_directory(self):
        for widget in self.main_view.winfo_children(): widget.destroy()
        ctk.CTkLabel(self.main_view, text="Customer Master Database", font=("Century Gothic", 30, "bold")).pack(pady=30, padx=60, anchor="w")
        
        table_frame = ctk.CTkFrame(self.main_view, fg_color="transparent")
        table_frame.pack(fill="both", expand=True, padx=60, pady=10)
        
        cols = ("ID", "Name", "CNIC", "Phone", "Total Debt")
        tree = ttk.Treeview(table_frame, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=180, anchor="center")
        tree.pack(fill="both", expand=True)
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT customer_id, full_name, cnic, phone, total_udhaar FROM customers")
        for row in cursor.fetchall():
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], f"Rs. {row[4]}"))
        conn.close()

    # --- 6. PAGE: CREDIT LOGS ---
    def draw_customer_logs(self):
        for widget in self.main_view.winfo_children(): widget.destroy()
        ctk.CTkLabel(self.main_view, text="Risk & Blacklist Registry", font=("Century Gothic", 30, "bold")).pack(pady=30, padx=60, anchor="w")

        table_container = ctk.CTkFrame(self.main_view, fg_color="transparent")
        table_container.pack(fill="both", expand=True, padx=60, pady=10)
        
        cols = ("Name", "Score", "Grade", "Safety Status")
        tree = ttk.Treeview(table_container, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=200, anchor="center")
        tree.pack(fill="both", expand=True)
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT c.full_name, s.score, s.grade FROM customers c JOIN credit_scores s ON c.customer_id = s.customer_id")
        for row in cursor.fetchall():
            risk_status = "🚨 BLACKLISTED" if row[1] < 40 else "✅ STABLE"
            tree.insert("", "end", values=(row[0], row[1], row[2], risk_status))
        conn.close()

    # --- 7. PAGE: ADD CUSTOMER ---
    def draw_add_customer(self):
        for widget in self.main_view.winfo_children(): widget.destroy()
        form_card = ctk.CTkFrame(self.main_view, width=650, height=550, corner_radius=30)
        form_card.place(relx=0.5, rely=0.5, anchor="center")
        form_card.pack_propagate(False)
        ctk.CTkLabel(form_card, text="Register Customer", font=("Century Gothic", 28, "bold")).pack(pady=40)
        self.name_entry = ctk.CTkEntry(form_card, placeholder_text="Full Name", width=420, height=55)
        self.name_entry.pack(pady=10)
        self.cnic_entry = ctk.CTkEntry(form_card, placeholder_text="CNIC", width=420, height=55)
        self.cnic_entry.pack(pady=10)
        self.phone_entry = ctk.CTkEntry(form_card, placeholder_text="Phone", width=420, height=55)
        self.phone_entry.pack(pady=10)
        ctk.CTkButton(form_card, text="ADD TO SYSTEM", command=self.save_customer, width=420, height=60, corner_radius=15, font=("Arial", 16, "bold")).pack(pady=30)

    def save_customer(self):
        if not self.name_entry.get(): return
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO customers (shop_id, full_name, cnic, phone) VALUES (1, %s, %s, %s)", 
                           (self.name_entry.get(), self.cnic_entry.get(), self.phone_entry.get()))
            cid = cursor.lastrowid
            cursor.execute("INSERT INTO credit_scores (customer_id, score, grade) VALUES (%s, 100, 'Excellent')", (cid,))
            conn.commit()
            messagebox.showinfo("Success", "Customer Profile Created.")
            self.draw_home()
        except Exception as e: messagebox.showerror("DB Error", str(e))
        finally: conn.close()

if __name__ == "__main__":
    app = SmartUdhaarApp()
    app.mainloop()
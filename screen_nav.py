screen_helper = """
#: import get_color_from_hex kivy.utils.get_color_from_hex
#:import NavigationLayout kivymd.uix.navigationdrawer.MDNavigationLayout
#:import Factory kivy.factory.Factory

ScreenManager:
    HomeScreen:
        name: 'home_screen'
    AdminLoginScreen:
        name: 'admin_login_screen'
    AdminHomeScreen:
        name: 'adminhome'
    AddLocationScreen:
        name: 'add_location_screen'
    ViewLocationScreen
        name: 'view_location_screen'
    AddCategoryScreen:
        name: 'add_category_screen'
    ViewCategoryScreen:
        name: 'view_category_screen'
    ViewProvidersScreen:
        name: 'view_providers_screen'
    ViewRequestScreen:
        name: 'view_request_screen'
    ViewHistoryScreen:
        name: 'view_history_screen'
    ViewPaymentsScreen:
        name: 'view_payments_screen'
    ViewCustomerComplaintsScreen:
        name: 'view_customer_complaint'
    ViewProviderComplaintsScreen:
        name: 'view_provider_complaint'


<AdminLoginScreen>
    admin_email: admin_email
    admin_password: admin_password
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        padding: dp(20)
        spacing: dp(10)
        Widget:
            size_hint_y: 1
        MDLabel:
            text: "ADMIN LOGIN"
            color: 1, 1, 0.6, 1  # Pale yellow color in RGBA format
            font_name: "Roboto"
            font_style: 'Button'
            font_size: sp(20)
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: dp(10)
        MDTextField:
            id: admin_email
            hint_text: "Email"
            font_name: "Roboto"
            icon_right: "account"
            mode: "round"
            size_hint_x: None
            width: dp(290)
            font_size: sp(15)
            pos_hint: {"center_x": 0.5}
            color_active: [1, 1, 1, 1]
            normal_color: [1, 1, 0, 1]
            on_text_validate: root.validate_provider_email(self)
        MDTextField:
            id: admin_password
            mode: "round"
            hint_text: "Password"
            font_name: "Roboto"
            icon_right: "eye-off"
            size_hint_x: None
            width: dp(290)
            font_size: sp(15)
            pos_hint: {"center_x": 0.5}
            color_active: [1, 1, 1, 1]
            password: True
            on_text: self.text = self.text.replace(" ", "")
            on_focus: admin_password.password = not self.focus
            MDIconButton:
                icon: "eye-off"
                pos_hint: {"center_y": 0.5}
                on_release: root.toggle_password_visibility()
        MDRoundFlatButton:
            text: "LOGIN"
            pos_hint: {"center_x": 0.5}
            font_size: sp(15)
            md_bg_color: 0.2, 0.2, 0.2, 1
            text_color: 1, 1, 1, 1
            on_press: root.admin_login()

<AdminHomeScreen>
    MDTopAppBar:
        title: "Snow Removal"
        pos_hint: {"top": 1}
        elevation: 10
    GridLayout:
        cols: 2
        spacing: dp(40)
        padding: dp(35)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": 0.6, "center_y": 0.5}
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: "80dp", "100dp"
            md_bg_color: 0, 0.5, 0.5, 1
            on_press: root.on_card_press('view_providers_screen')
            MDLabel:
                text: "View Providers"
                font_size: sp(15)
                font_name: "Roboto"
                halign: "center"
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: "80dp", "100dp"
            md_bg_color: 0, 0.5, 0.5, 1
            on_press: root.on_card_press('add_location_screen')
            MDLabel:
                text: "Add Locations"
                font_size: sp(15)
                font_name: "Roboto"
                halign: "center"
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: "80dp", "100dp"
            md_bg_color: 0, 0.5, 0.5, 1
            on_press: root.on_card_press('view_location_screen')
            MDLabel:
                text: "View Locations"
                font_size: sp(15)
                font_name: "Roboto"
                halign: "center"
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: "80dp", "100dp"
            md_bg_color: 0, 0.5, 0.5, 1
            on_press: root.on_card_press('add_category_screen')
            MDLabel:
                text: "Add Category"
                font_size: sp(15)
                font_name: "Roboto"
                halign: "center"
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: "80dp", "100dp"
            md_bg_color: 0, 0.5, 0.5, 1
            on_press: root.on_card_press('view_category_screen')
            MDLabel:
                text: "View Category"
                font_size: sp(15)
                font_name: "Roboto"
                halign: "center"
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: "80dp", "100dp"
            md_bg_color: 0, 0.5, 0.5, 1
            on_press: root.on_card_press('view_request_screen')
            MDLabel:
                text: "View Requests"
                font_size: sp(15)
                font_name: "Roboto"
                halign: "center"
        MDCard:
            orientation: 'vertical'
            size_hint: None, None
            size: "80dp", "100dp"
            md_bg_color: 0, 0.5, 0.5, 1
            on_press: root.on_card_press('view_history_screen')
            MDLabel:
                text: "View History"
                font_size: sp(15)
                font_name: "Roboto"
                halign: "center"
    BoxLayout:
        orientation: 'vertical'
        size_hint: None, None
        size: "200dp", "50dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        MDRaisedButton:
            text: "Logout"
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {"center_x": 0.5}
            on_release: root.manager.current = 'admin_login_screen'

<AddLocationScreen>
    permissions_granted: root.permissions_granted
    on_permissions_granted: root.on_permissions_granted(*args)
    location_name : location_name
    zip_code: zip_code
    MDCard:
        size_hint: None, None
        size: dp(450), dp(600)
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 5
        md_bg_color: [0, 0, 0, 1]
        padding: dp(9)
        spacing: dp(10)
        orientation: "vertical"
        MDLabel:
            text: "Add Location"
            font_size: sp(30)
            font_name: "Roboto"
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            color: 1, 0.647, 0, 1
        Widget:
            size_hint_y: None
            height: dp(40)
        Spinner:
            id: state_spinner
            pos_hint: {"center_x": .5}
            font_name: "Roboto"
            text: 'Select State'
            size_hint_x: None
            width: dp(290)
            height: dp(40)
            md_bg_color: [0.2, 0.2, 0.2, 1]
            text_color: [1, 1, 1, 1]
            values: ["New Hampshire", "Maine", "Vermont", "Alaska", "Wyoming", "Michigan", "New York", "Utah", "Minnesota", "Massachusetts"]
            on_text: root.update_city_spinner(self.text)
        Widget:
            size_hint_y: None
            height: dp(10)
        Spinner:
            id: city_spinner
            pos_hint: {"center_x": .5}
            font_name: "Roboto"
            text: 'Select City'
            size_hint_x: None
            width: dp(290)
            height: dp(40)
            md_bg_color: [0.2, 0.2, 0.2, 1]
            text_color: [1, 1, 1, 1]
        Widget:
            size_hint_y: None
            height: dp(20)
        MDTextField:
            id : location_name
            hint_text: "Location Name"
            font_name: "Roboto"
            size_hint_x: None
            width: dp(290)
            height: dp(40)
            font_size: sp(20)
            pos_hint: {"center_x": .5}
            color_active: [1, 0.647, 0, 1]
            normal_color: [1, 1, 1, 1]
        MDTextField:
            id : zip_code
            hint_text: "Zip Code"
            font_name: "Roboto"
            size_hint_x: None
            width: dp(290)
            height: dp(40)
            font_size: sp(20)
            pos_hint: {"center_x": .5}
            color_active: [1, 0.647, 0, 1]
            normal_color: [1, 1, 1, 1]
        MDRoundFlatButton:
            id: location_picture
            text: "Select Location Picture"
            pos_hint: {"center_x": .5}
            font_size: sp(20)
            text_color: [1, 1, 1, 1]
            md_bg_color: [0, 0.502, 0.502, 1]
            on_press: root.location_button()
        Widget:
            size_hint_y: None
            height: dp(10)
        Image:
            id : location_picture
            size_hint: None, None
            size: dp(100), dp(100)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            allow_stretch: True
            keep_ratio: True
            height: dp(100)
            opacity: 0
        MDRoundFlatButton:
            text: "ADD LOCATION"
            pos_hint: {"center_x": .5}
            font_size: sp(20)
            on_press: root.add_location_data()
    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {"center_x": .5}
        font_size: sp(20)
        on_press: root.manager.current='adminhome'

<ViewLocationScreen>
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)  # Use dp for padding
        ScrollView:
            GridLayout:
                id: location_table_layout
                cols: 1
                spacing: dp(20)  # Use dp for spacing
                size_hint_y: None
                height: self.minimum_height
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {"center_x": .5}
            font_size: sp(20)  # Use sp for font size
            on_press: root.manager.current='adminhome'

<AddCategoryScreen>
    category_name : category_name
    MDCard:
        size_hint: None, None
        size: dp(450), dp(500)  # Use dp for sizes
        pos_hint: {"center_x":.5, "center_y":.5}
        elevation: dp(5)  # Use dp for elevation
        md_bg_color: [0, 0, 0, 1]  # Black color (RGBA)
        padding: dp(9)  # Use dp for padding
        spacing: dp(10)  # Use dp for spacing
        orientation: "vertical"
        MDLabel:
            text: "Add Category"
            font_size: sp(30)  # Use sp for font size
            font_name: "Roboto"
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            color: 1, 0.647, 0, 1  # Orange color (RGBA)
        Widget:
            size_hint_y: None
            height: dp(40)  # Use dp for height
        MDTextField:
            id: category_name
            hint_text: "Category Name"
            font_name: "Roboto"
            size_hint_x: None
            width: dp(290)  # Use dp for width
            font_size: sp(20)  # Use sp for font size
            pos_hint: {"center_x": .5}
            color_active: 1, 0.647, 0, 1  # Orange (RGBA)
            normal_color: 1, 1, 1, 1  # White (RGBA)
        MDRoundFlatButton:
            id: category_picture
            text: "Select Category Picture"
            pos_hint: {"center_x": .5}
            font_size: sp(20)  # Use sp for font size
            text_color: 1, 1, 1, 1  # RGBA values for white
            md_bg_color: 0, 0.502, 0.502, 1  # Teal color in RGBA format
            on_press : root.category_button()
        Widget:
            size_hint_y: None
            height: dp(10)  # Use dp for height
        Image:
            id: category_image
            size_hint: None, None
            size: dp(100), dp(100)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            allow_stretch: True
            keep_ratio: True
            height: dp(100)  # Use dp for height
            opacity: 0 
        MDRoundFlatButton:
            text: "ADD CATEGORY"
            pos_hint: {"center_x": .5}
            font_size: sp(20)  # Use sp for font size
            on_press: root.add_category_data()
    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {"center_x": .5}
        font_size: sp(20)  # Use sp for font size
        on_press: root.manager.current='adminhome'

<ViewCategoryScreen>
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)  # Use dp for padding
        ScrollView:
            GridLayout:
                id: category_table_layout
                cols: 1  # Set to 1 since we want one card per row
                spacing: dp(20)  # Use dp for spacing between the cards
                size_hint_y: None
                height: self.minimum_height  # Add this line
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {"center_x": .5}
            font_size: sp(20)  # Use sp for font size
            on_press: root.manager.current='adminhome'

<ViewProvidersScreen>
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)  # Use dp for padding
        ScrollView:
            GridLayout:
                id: admin_view_provider_cards_layout
                cols: 1
                spacing: dp(10)  # Use dp for spacing
                size_hint_y: None
                height: self.minimum_height
                padding: dp(5)  # Use dp for padding
    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {"center_x": .5}
        font_size: sp(20)  # Use sp for font size
        on_press: root.manager.current='adminhome'

<ViewRequestScreen>
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': 0.4}
        padding: dp(20)  # Use dp for padding
        spacing: dp(10)
        ScrollView:
            GridLayout:
                id: admin_service_cards_layout
                cols: 1  # Set to 1 since we want one card per row
                size_hint_y: None
                height: self.minimum_height
                padding: dp(5)  # Use dp for padding
                spacing: dp(10)  # Use dp for spacing
    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {"center_x": .5}
        font_size: sp(20)  # Use sp for font size
        on_press: root.manager.current='adminhome'

<ViewHistoryScreen>
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': 0.4}
        padding: dp(50)  # Use dp for padding
        spacing: dp(10)
        ScrollView:
            GridLayout:
                id: admin_view_history_layout
                cols: 1  # Set to 1 since we want one card per row
                size_hint_y: None
                height: self.minimum_height
                padding: dp(5)  # Use dp for padding
                spacing: dp(10)  # Use dp for spacing
    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {"center_x": .5}
        font_size: sp(20)  # Use sp for font size
        on_press: root.manager.current='adminhome'

<ViewPaymentsScreen>
    BoxLayout:
        orientation: 'vertical'
        padding: dp(50)  # Use dp for padding
        spacing: dp(10)  # Use dp for spacing
        ScrollView:
            GridLayout:
                id: view_payment_layout
                cols: 4  # Set to 1 since we want one card per row
                spacing: dp(20)  # Use dp for spacing between the cards
    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {"center_x": .5}
        font_size: sp(20)  # Use sp for font size
        on_press: root.manager.current='adminhome'

<ViewCustomerComplaintsScreen>
    BoxLayout:
        orientation: 'vertical'
        padding: dp(50)  # Use dp for padding
        spacing: dp(20)  # Use dp for spacing
        ScrollView:
            GridLayout:
                id: view_complaints_screen
                cols: 1  # Set to 1 since we want one card per row
                spacing: dp(20)  # Use dp for spacing between the cards
    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {"center_x": .5}
        font_size: sp(20)  # Use sp for font size
        on_press: root.manager.current='adminhome'

<ViewProviderComplaintsScreen>
    BoxLayout:
        orientation: 'vertical'
        padding: dp(50)  # Use dp for padding
        spacing: dp(20)  # Use dp for spacing
        ScrollView:
            GridLayout:
                id: view_provider_complaints_screen
                cols: 1  # Set to 1 since we want one card per row
                spacing: dp(20)  # Use dp for spacing between the cards
    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {"center_x": .5}
        font_size: sp(20)  # Use sp for font size
        on_press: root.manager.current='adminhome'
"""
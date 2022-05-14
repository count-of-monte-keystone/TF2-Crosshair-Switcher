import tkinter, os, re
from tkinter import messagebox

class Model:
    
    crosshairs_directory = ""
    
    weapon_scripts_directory = ""
    
    desired_crosshair = ""
    
    available_weapons = []
    
    available_crosshairs = []
    
    class_categories = ["Scout", "Soldier", "Demoman", "Medic", "Sniper", "Engineer", "Pyro", "Spy", "Heavy"]
    
    weapon_categories = ["Primary", "Secondary", "Melee", "Misc."]
    
    scout_weapons = ["tf_weapon_bat_fish","tf_weapon_bat_giftwrap","tf_weapon_bat_wood","tf_weapon_handgun_scout_primary","tf_weapon_handgun_scout_secondary","tf_weapon_pistol_scout",
                     "tf_weapon_scattergun","tf_weapon_soda_popper","tf_weapon_cleaver","tf_weapon_jar_milk","tf_weapon_lunchbox_drink"
                     ]
                     
    soldier_weapons = ["tf_weapon_rocketlauncher","tf_weapon_rocketlauncher_airstrike","tf_weapon_rocketlauncher_directhit","tf_weapon_shotgun_soldier",
                       "tf_weapon_shovel","tf_weapon_katana","tf_weapon_buff_item","tf_weapon_particle_cannon","tf_weapon_raygun"
                       ]
                       
    demoman_weapons = ["tf_weapon_grenadelauncher","tf_weapon_katana","tf_weapon_stickbomb","tf_weapon_sword","tf_weapon_pipebomblauncher","tf_weapon_cannon","tf_weapon_bottle"]    
    
    medic_weapons = ["tf_weapon_syringegun_medic","tf_weapon_medigun","tf_weapon_crossbow","tf_weapon_bonesaw"]
    
    sniper_weapons = ["tf_weapon_sniperrifle","tf_weapon_sniperrifle_classic","tf_weapon_sniperrifle_decap","tf_weapon_club","tf_weapon_charged_smg","tf_weapon_compound_bow",
                      "tf_weapon_smg","tf_weapon_jar"
                      ]
                      
    engineer_weapons = ["tf_weapon_wrench","tf_weapon_shotgun_building_rescue","tf_weapon_shotgun_primary","tf_weapon_drg_pomson","tf_weapon_mechanical_arm","tf_weapon_robot_arm",
                        "tf_weapon_builder","tf_weapon_objectselection","tf_weapon_pda_engineer_build","tf_weapon_pda_engineer_destroy","tf_weapon_pistol","tf_weapon_sentry_revenge"
                        ]
                        
    pyro_weapons = ["tf_weapon_flamethrower","tf_weapon_fireaxe","tf_weapon_flaregun","tf_weapon_flaregun_revenge","tf_weapon_shotgun_pyro","tf_weapon_rocketlauncher_fireball",
                    "tf_weapon_rocketpack","tf_weapon_slap"
                    ]
                    
    spy_weapons = ["tf_weapon_knife","tf_weapon_revolver","tf_weapon_invis","tf_weapon_sapper","tf_weapon_pda_spy"]
    
    heavy_weapons = ["tf_weapon_minigun","tf_weapon_shotgun_hwg","tf_weapon_fists","tf_weapon_lunchbox"]
    
    primary_weapons = ["tf_weapon_cannon","tf_weapon_flamethrower","tf_weapon_grenadelauncher","tf_weapon_shotgun_primary","tf_weapon_minigun","tf_weapon_sniperrifle",
                       "tf_weapon_sniperrifle_classic","tf_weapon_sniperrifle_decap","tf_weapon_soda_popper","tf_weapon_syringegun_medic","tf_weapon_scattergun",
                       "tf_weapon_sentry_revenge","tf_weapon_pep_brawler_blaster","tf_weapon_drg_pomson","tf_weapon_crossbow","tf_weapon_compound_bow","tf_weapon_particle_cannon",
                       "tf_weapon_shotgun_building_rescue","tf_weapon_rocketlauncher","tf_weapon_rocketlauncher_airstrike","tf_weapon_rocketlauncher_directhit",
                       "tf_weapon_handgun_scout_primary","tf_weapon_rocketlauncher_fireball"
                       ]
                       
    secondary_weapons = ["tf_weapon_mechanical_arm","tf_weapon_jar","tf_weapon_jar_milk","tf_weapon_lunchbox","tf_weapon_revolver","tf_weapon_medigun","tf_weapon_cleaver",
                         "tf_weapon_smg","tf_weapon_handgun_scout_secondary","tf_weapon_pistol","tf_weapon_pistol_scout","tf_weapon_flaregun","tf_weapon_flaregun_revenge",
                         "tf_weapon_raygun","tf_weapon_shotgun_hwg","tf_weapon_shotgun_pyro","tf_weapon_shotgun_soldier","tf_weapon_laser_pointer","tf_weapon_charged_smg",
                         "tf_weapon_lunchbox_drink","tf_weapon_pipebomblauncher","tf_weapon_buff_item","tf_weapon_rocketpack"
                         ]
                         
    melee_weapons = ["tf_weapon_bat_fish","tf_weapon_bat_giftwrap","tf_weapon_bat_wood","tf_weapon_bottle","tf_weapon_club","tf_weapon_fists","tf_weapon_katana",
                     "tf_weapon_sword","tf_weapon_wrench","tf_weapon_robot_arm","tf_weapon_stickbomb","tf_weapon_bonesaw","tf_weapon_fireaxe","tf_weapon_knife",
                     "tf_weapon_shovel","tf_weapon_slap"
                     ]
                     
    misc_weapons = ["tf_weapon_parachute","tf_weapon_parachute_primary","tf_weapon_parachute_secondary","tf_weapon_spellbook","tf_weapon_grapplinghook",
                    "tf_weapon_builder","tf_weapon_invis","tf_weapon_objectselection","tf_weapon_pda_engineer_build","tf_weapon_pda_engineer_destroy",
                    "tf_weapon_passtime_gun"
                    ]
    #lists below refer to the default x, y, width, and height values for the crosshairs of the weapons in them               
    all_32s = ["tf_weapon_bat_fish","tf_weapon_bat_giftwrap","tf_weapon_bat_wood","tf_weapon_bottle","tf_weapon_buff_item","tf_weapon_cannon","tf_weapon_cleaver","tf_weapon_club","tf_weapon_fists",
               "tf_weapon_flamethrower","tf_weapon_grenadelauncher","tf_weapon_katana","tf_weapon_parachute","tf_weapon_parachute_primary","tf_weapon_parachute_secondary","tf_weapon_particle_cannon",
               "tf_weapon_passtime_gun","tf_weapon_pipebomblauncher","tf_weapon_robot_arm","tf_weapon_rocketlauncher","tf_weapon_rocketlauncher_airstrike","tf_weapon_rocketlauncher_directhit",
               "tf_weapon_shotgun_building_rescue","tf_weapon_shovel","tf_weapon_spellbook","tf_weapon_stickbomb","tf_weapon_sword","tf_weapon_wrench"
               ]
               
    all_64s = ["tf_weapon_minigun"]
    
    _0_0_32_32 = ["tf_weapon_charged_smg","tf_weapon_compound_bow","tf_weapon_crossbow","tf_weapon_drg_pomson","tf_weapon_flaregun","tf_weapon_flaregun_revenge","tf_weapon_grapplinghook",
                  "tf_weapon_handgun_scout_primary","tf_weapon_handgun_scout_secondary","tf_weapon_mechanical_arm","tf_weapon_pep_brawler_blaster","tf_weapon_pistol","tf_weapon_pistol_scout",
                  "tf_weapon_raygun","tf_weapon_scattergun","tf_weapon_sentry_revenge","tf_weapon_shotgun_hwg","tf_weapon_shotgun_primary","tf_weapon_shotgun_pyro","tf_weapon_shotgun_soldier",
                  "tf_weapon_smg","tf_weapon_soda_popper","tf_weapon_syringegun_medic"
                  ]
                  
    _64_0_32_32 = ["tf_weapon_bonesaw","tf_weapon_fireaxe","tf_weapon_knife","tf_weapon_laser_pointer","tf_weapon_revolver","tf_weapon_sniperrifle","tf_weapon_sniperrifle_classic",
                   "tf_weapon_sniperrifle_decap"
                   ]
                   
    _0_64_32_32 = ["tf_weapon_medigun"]
    
    _0_48_24_24 = ["tf_weapon_builder","tf_weapon_invis","tf_weapon_jar","tf_weapon_jar_milk","tf_weapon_lunchbox","tf_weapon_lunchbox_drink","tf_weapon_objectselection",
                   "tf_weapon_pda_engineer_build","tf_weapon_pda_engineer_destroy","tf_weapon_pda_spy","tf_weapon_sapper"
                   ]
    
    @staticmethod
    def get_weapon_script_text(script_name):
        extracted_text = None
        file = open(Model.weapon_scripts_directory+"/"+script_name+".txt", mode='r')
        extracted_text = file.readlines()
        return extracted_text
    
    @staticmethod
    def get_crosshair_position_values(script_text):
        file_index = None
        x_index = None
        y_index = None
        width_index = None
        height_index = None
        for i in range(len(script_text)):
            if script_text[i].find("\"crosshair\"") >= 0:
                file_index = i+2
                x_index = i+3
                y_index = i+4
                width_index = i+5
                height_index = i+6
                break
        return file_index, x_index, y_index, width_index, height_index
    
    @staticmethod
    def get_old_value(text_line, line_type):
        if(line_type == "file"):
            file_path_part = text_line.split("\"file\"")
            pattern = "\"(.*)\""
            actual_filepath = re.findall(pattern, file_path_part[1])
            return actual_filepath[0]
        elif(line_type == "x"):
            x_value_part = text_line.split("\"x\"")
            pattern = "\"(.*)\""
            actual_x = re.findall(pattern, x_value_part[1])
            return actual_x[0]
        elif(line_type == "y"):
            y_value_part = text_line.split("\"y\"")
            pattern = "\"(.*)\""
            actual_y = re.findall(pattern, y_value_part[1])
            return actual_y[0]
        elif(line_type == "width"):
            width_value_part = text_line.split("\"width\"")
            pattern = "\"(.*)\""
            actual_width = re.findall(pattern, width_value_part[1])
            return actual_width[0]
        else:
            height_value_part = text_line.split("\"height\"")
            pattern = "\"(.*)\""
            actual_height = re.findall(pattern, height_value_part[1])
            return actual_height[0]
    
    @staticmethod        
    def determine_default_values(weapon_script):
        if weapon_script in Model.all_32s:
            return "32,32,32,32"
        elif weapon_script in Model.all_64s:
            return "64,64,64,64"
        elif weapon_script in Model._0_0_32_32:
            return "0,0,32,32"
        elif weapon_script in Model._0_48_24_24:
            return "0,48,24,24"
        elif weapon_script in Model._0_64_32_32:
            return "0,64,32,32"
        else:
            return "64,0,32,32"
    
    @staticmethod
    def generate_crosshair_values_list(weapon_list):
        crosshair_section_values = []
        for weapon_script in weapon_list:
            script_data = []
            script_data.append(weapon_script)
            text = Model.get_weapon_script_text(weapon_script)
            script_data.append(text)
            file_line_index = Model.get_crosshair_position_values(text)[0]
            script_data.append(file_line_index)
            x_line_index = Model.get_crosshair_position_values(text)[1]
            script_data.append(x_line_index)
            y_line_index = Model.get_crosshair_position_values(text)[2]
            script_data.append(y_line_index)
            width_line_index = Model.get_crosshair_position_values(text)[3]
            script_data.append(width_line_index)
            height_line_index = Model.get_crosshair_position_values(text)[4]
            script_data.append(height_line_index)
            crosshair_section_values.append(script_data)
        return crosshair_section_values
    
    @staticmethod
    def set_new_crosshair_values(crosshair_values):
        script_name = crosshair_values[0]
        script_text = crosshair_values[1]
        file_index = crosshair_values[2]
        x_index = crosshair_values[3]
        y_index = crosshair_values[4]
        width_index = crosshair_values[5]
        height_index = crosshair_values[6]
    
        current_filepath = Model.get_old_value(script_text[file_index], "file")
        current_x = Model.get_old_value(script_text[x_index], "x")
        current_y = Model.get_old_value(script_text[y_index], "y")
        current_width = Model.get_old_value(script_text[width_index], "width")
        current_height = Model.get_old_value(script_text[height_index], "height")
    
        if Model.desired_crosshair == "default":
            new_filepath = "sprites/crosshairs"
            script_text[file_index] = script_text[file_index].replace(current_filepath, new_filepath)
            if Model.determine_default_values(script_name) == "32,32,32,32":
                script_text[x_index] = script_text[x_index].replace(current_x, "32")              
                script_text[y_index] = script_text[y_index].replace(current_y, "32")
                script_text[width_index] = script_text[width_index].replace(current_width, "32")
                script_text[height_index] = script_text[height_index].replace(current_height, "32")
                with open(Model.weapon_scripts_directory+"/"+script_name+".txt", "w") as updated_script:
                    for line in script_text:
                        updated_script.write(line)
            elif Model.determine_default_values(script_name) == "64,64,64,64":
                script_text[x_index] = script_text[x_index].replace(current_x, "64")              
                script_text[y_index] = script_text[y_index].replace(current_y, "64")
                script_text[width_index] = script_text[width_index].replace(current_width, "64")
                script_text[height_index] = script_text[height_index].replace(current_height, "64")
                with open(Model.weapon_scripts_directory+"/"+script_name+".txt", "w") as updated_script:
                    for line in script_text:
                        updated_script.write(line)
            elif Model.determine_default_values(script_name) == "0,0,32,32":
                script_text[x_index] = script_text[x_index].replace(current_x, "0")              
                script_text[y_index] = script_text[y_index].replace(current_y, "0")
                script_text[width_index] = script_text[width_index].replace(current_width, "32")
                script_text[height_index] = script_text[height_index].replace(current_height, "32")
                with open(Model.weapon_scripts_directory+"/"+script_name+".txt", "w") as updated_script:
                    for line in script_text:
                        updated_script.write(line)
            elif Model.determine_default_values(script_name) == "0,48,24,24":
                script_text[x_index] = script_text[x_index].replace(current_x, "0")              
                script_text[y_index] = script_text[y_index].replace(current_y, "48")
                script_text[width_index] = script_text[width_index].replace(current_width, "24")
                script_text[height_index] = script_text[height_index].replace(current_height, "24")
                with open(Model.weapon_scripts_directory+"/"+script_name+".txt", "w") as updated_script:
                    for line in script_text:
                        updated_script.write(line)
            elif Model.determine_default_values(script_name) == "0,64,32,32":
                script_text[x_index] = script_text[x_index].replace(current_x, "0")              
                script_text[y_index] = script_text[y_index].replace(current_y, "64")
                script_text[width_index] = script_text[width_index].replace(current_width, "32")
                script_text[height_index] = script_text[height_index].replace(current_height, "32")
                with open(Model.weapon_scripts_directory+"/"+script_name+".txt", "w") as updated_script:
                    for line in script_text:
                        updated_script.write(line)
            else:
                script_text[x_index] = script_text[x_index].replace(current_x, "64")              
                script_text[y_index] = script_text[y_index].replace(current_y, "0")
                script_text[width_index] = script_text[width_index].replace(current_width, "32")
                script_text[height_index] = script_text[height_index].replace(current_height, "32")
                with open(Model.weapon_scripts_directory+"/"+script_name+".txt", "w") as updated_script:
                    for line in script_text:
                        updated_script.write(line)            
        else:
            new_filepath = Model.crosshairs_directory
            new_filepath = new_filepath.split("materials/")[1]+"/"+Model.desired_crosshair
            script_text[file_index] = script_text[file_index].replace(current_filepath, new_filepath)
            script_text[x_index] = script_text[x_index].replace(current_x, "0")              
            script_text[y_index] = script_text[y_index].replace(current_y, "0")
            script_text[width_index] = script_text[width_index].replace(current_width, "64")
            script_text[height_index] = script_text[height_index].replace(current_height, "64")
            with open(Model.weapon_scripts_directory+"/"+script_name+".txt", "w") as updated_script:
                for line in script_text:
                    updated_script.write(line)        
    
    @staticmethod
    def validate_directory(path, directory_type):
        if os.path.isdir(path):
            if directory_type == "weapon scripts directory":
                keywords = ["\\steamapps\\","\\common\\","\\Team Fortress 2\\","\\tf\\","\\custom\\"]
                keyword_counter = 0
                for keyword in keywords:
                    if path.find(keyword) >=0:
                        keyword_counter += 1
                if keyword_counter == 5:
                    weapon_files = 0
                    for file_name in os.listdir(path):
                        if file_name.startswith("tf_") and file_name.endswith(".txt"):
                            weapon_files+=1
                    if weapon_files >= 1:
                        Model.weapon_scripts_directory = path.replace("\\", "/")
                        return True
                    else:
                        return False
                else:
                    return False        
            else:
                keywords = ["\\steamapps\\","\\common\\","\\Team Fortress 2\\","\\tf\\","\\materials\\","\\vgui\\","\\replay\\","\\thumbnails"]
                keyword_counter = 0
                for keyword in keywords:
                    if path.find(keyword) >= 0:
                        keyword_counter += 1
                if keyword_counter == 8:
                    vmt_files = 0
                    vtf_files = 0
                    for file_name in os.listdir(path):
                        if file_name.endswith(".vmt"):
                            vmt_files+=1
                        elif file_name.endswith(".vtf"):
                            vtf_files+=1
                    if vtf_files >= 1 and vmt_files >=1:
                        if vtf_files == vmt_files:
                            Model.crosshairs_directory = path.replace("\\", "/")
                            return True
                        elif vtf_files > vmt_files:
                            return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            return False

    @staticmethod
    def generate_crosshairs_list(crosshairs_directory):
        crosshair_options = ["default"]
        for crosshair_file in os.listdir(crosshairs_directory):
            if crosshair_file.endswith(".vtf"):
                crosshair_options.append(crosshair_file.replace(".vtf", ""))
        Model.available_crosshairs = crosshair_options        
        return crosshair_options    
        
    @staticmethod
    def generate_weapons_list(scripts_directory):
        weapon_scripts_options = []
        for script_file in os.listdir(scripts_directory):
            if script_file.startswith("tf_"):
                weapon_scripts_options.append(script_file.replace(".txt",""))
        Model.available_weapons = weapon_scripts_options        
        return weapon_scripts_options

    @staticmethod
    def modify_weapon_scripts(apply_to, crosshair_to_apply):#make an optional parameter here and in set_new_crosshair_values for desired_crosshair
        Model.desired_crosshair = crosshair_to_apply
        if apply_to == "All classes/weapons":
            all_data = Model.generate_crosshair_values_list(Model.available_weapons)
            for list in all_data:
                Model.set_new_crosshair_values(list)
                
        elif apply_to in Model.class_categories:
            if apply_to == "Scout":
                scout_data = Model.generate_crosshair_values_list(Model.scout_weapons)
                for list in scout_data:
                    Model.set_new_crosshair_values(list)
            elif apply_to == "Soldier":
                soldier_data = Model.generate_crosshair_values_list(Model.soldier_weapons)
                for list in soldier_data:
                    Model.set_new_crosshair_values(list)
            elif apply_to == "Demoman":
                demoman_data = Model.generate_crosshair_values_list(Model.demoman_weapons)
                for list in demoman_data:
                    Model.set_new_crosshair_values(list)
            elif apply_to == "Medic":
                medic_data = Model.generate_crosshair_values_list(Model.medic_weapons)
                for list in medic_data:
                    Model.set_new_crosshair_values(list)
            elif apply_to == "Sniper":
                sniper_data = Model.generate_crosshair_values_list(Model.sniper_weapons)
                for list in sniper_data:
                    Model.set_new_crosshair_values(list)
            elif apply_to == "Engineer":
                engie_data = Model.generate_crosshair_values_list(Model.engineer_weapons)
                for list in engie_data:
                    Model.set_new_crosshair_values(list)
            elif apply_to == "Pyro":
                pyro_data = Model.generate_crosshair_values_list(Model.pyro_weapons)
                for list in pyro_data:
                    Model.set_new_crosshair_values(list)
            elif apply_to == "Spy":
                spy_data = Model.generate_crosshair_values_list(Model.spy_weapons)
                for list in spy_data:
                    Model.set_new_crosshair_values(list)
            else:
                heavy_data = Model.generate_crosshair_values_list(Model.heavy_weapons)
                for list in heavy_data:
                    Model.set_new_crosshair_values(list)
            
        elif apply_to in Model.weapon_categories:
            if apply_to == "Primary":
                primary_data = Model.generate_crosshair_values_list(Model.primary_weapons)
                for list in primary_data:
                    Model.set_new_crosshair_values(list)
            elif apply_to == "Secondary":
                secondary_data = Model.generate_crosshair_values_list(Model.secondary_weapons)
                for list in secondary_data:
                    Model.set_new_crosshair_values(list)
            elif apply_to == "Melee":
                melee_data = Model.generate_crosshair_values_list(Model.melee_weapons)
                for list in melee_data:
                    Model.set_new_crosshair_values(list)
            else:
                misc_data = Model.generate_crosshair_values_list(Model.misc_weapons)
                for list in misc_data:
                    Model.set_new_crosshair_values(list)
                    
        else:
            script_data = []
            script_data.append(apply_to)
            text = Model.get_weapon_script_text(apply_to)
            script_data.append(text)
            file_line_index = Model.get_crosshair_position_values(text)[0]
            script_data.append(file_line_index)
            x_line_index = Model.get_crosshair_position_values(text)[1]
            script_data.append(x_line_index)
            y_line_index = Model.get_crosshair_position_values(text)[2]
            script_data.append(y_line_index)
            width_line_index = Model.get_crosshair_position_values(text)[3]
            script_data.append(width_line_index)
            height_line_index = Model.get_crosshair_position_values(text)[4]
            script_data.append(height_line_index)
            Model.set_new_crosshair_values(script_data)
        
class View(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.geometry("500x500")
        self.title("TF2 Crosshair Switcher")
        
        container_frame = tkinter.Frame(self)
        container_frame.pack(side="top", fill="both", expand=True)
        container_frame.grid_rowconfigure(0, weight=1)
        container_frame.grid_columnconfigure(0, weight=1)
        
        self._directory_frame = DirectoryFrame(container_frame)
        self._directory_frame.grid(row=0, column=0, sticky="nsew")
        self._crosshairs_frame = CrosshairsFrame(container_frame)
        self._crosshairs_frame.grid(row=0, column=0, sticky="nsew")
        self._scripts_frame = ScriptsFrame(container_frame)
        self._scripts_frame.grid(row=0, column=0, sticky="nsew")
        
    @property
    def directory_frame(self):
        return self._directory_frame
        
    @property
    def crosshairs_frame(self):
        return self._crosshairs_frame
        
    @property
    def scripts_frame(self):
        return self._scripts_frame                    
        
class DirectoryFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        for row in range(7):
            for column in range(7):
                self.grid_rowconfigure(row, weight=1)
                self.grid_columnconfigure(column, weight=1)
        
        #important widgets need to be tied to the object
        crosshairs_directory_label = tkinter.Label(self, text="Crosshairs Directory:")
        crosshairs_directory_label.grid(row=1, column=0)
        self._crosshairs_directory_entry = tkinter.Entry(self, bd=5)
        self._crosshairs_directory_entry.grid(row=1, column=1)
        
        scripts_directory_label = tkinter.Label(self, text="Weapon Scripts Directory:")
        scripts_directory_label.grid(row=2, column=0)
        self._scripts_directory_entry = tkinter.Entry(self, bd=5)
        self._scripts_directory_entry.grid(row=2, column=1)
        
        self._submit_button = tkinter.Button(self, text='Submit', fg="green", width=15)
        self._submit_button.grid(row=3, column=1)
        
        self._quit_button = tkinter.Button(self, text='Quit', fg="red", width=15)
        self._quit_button.grid(row=4, column=1)
        
    @property
    def crosshairs_directory_entry(self):
        return self._crosshairs_directory_entry
        
    @property     
    def scripts_directory_entry(self):
        return self._scripts_directory_entry
        
    @property
    def submit_button(self):
        return self._submit_button
        
    @property
    def quit_button(self):
        return self._quit_button
             
class CrosshairsFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        for row in range(9):
            for column in range(9):
                self.grid_rowconfigure(row, weight=1)
                self.grid_columnconfigure(column, weight=1)
        
        available_crosshairs_list = ["placeholder"]
        self._selected_crosshair = tkinter.StringVar(self)
        self._crosshairs_menu = tkinter.OptionMenu(self, self._selected_crosshair, *available_crosshairs_list)
        self._crosshairs_menu.grid(row=0, column=4)
        
        self._submit_button = tkinter.Button(self, text='Submit', fg="green", width=15)
        self._submit_button.grid(row=1, column=2)
       
        self._quit_button = tkinter.Button(self, text='Quit', fg="red", width=15)
        self._quit_button.grid(row=2, column=2)    
      
    @property    
    def selected_crosshair(self):
        return self._selected_crosshair
      
    @property
    def crosshairs_menu(self):
        return self._crosshairs_menu
 
    @property
    def submit_button(self):
        return self._submit_button
        
    @property
    def quit_button(self):
        return self._quit_button
    
class ScriptsFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        for row in range(9):
            for column in range(9):
                self.grid_rowconfigure(row, weight=1)
                self.grid_columnconfigure(column, weight=1)
        
        broad_options_list = ["All classes/weapons", "Specific class", "Specific weapon", "Specific weapon type"]
        self._selected_broad_option = tkinter.StringVar(self)
        self._selected_broad_option.set(broad_options_list[0])
        broad_options_menu = tkinter.OptionMenu(self, self._selected_broad_option, *broad_options_list)
        broad_options_menu.grid(row=0, column=4)
        
        classes_list = ["Scout", "Soldier", "Pyro", "Demoman", "Heavy", "Engineer", "Medic", "Sniper", "Spy"]
        self._selected_class = tkinter.StringVar(self)
        self._selected_class.set(classes_list[0])
        self._classes_menu = tkinter.OptionMenu(self, self._selected_class, *classes_list)
        
        weapons_list = ["placeholder"]
        self._selected_weapon = tkinter.StringVar(self)
        self._weapons_menu = tkinter.OptionMenu(self, self._selected_weapon, *weapons_list)
        
        weapon_type_list = ["Primary", "Secondary", "Melee", "Misc."]
        self._selected_weapon_type = tkinter.StringVar(self)
        self._selected_weapon_type.set(weapon_type_list[0])
        self._weapon_types_menu = tkinter.OptionMenu(self, self._selected_weapon_type, *weapon_type_list)
        
        #need to assign commands to the broad options so that, when clicked, they display their further lists (nothing for all)
        #picking a certain class should display a list with the broad options (minus the specific class one)
        #clicking submit will process everthing that the user has selected from the visible lists at the time they click submit
        self._submit_button = tkinter.Button(self, text='Submit', fg="green", width=15)
        self._submit_button.grid(row=1, column=2)
        
        self._back_button = tkinter.Button(self, text='Back', fg="orange", width=15)
        self._back_button.grid(row=2, column=2)
       
        self._quit_button = tkinter.Button(self, text='Quit', fg="red", width=15)
        self._quit_button.grid(row=3, column=2)
                
    @property
    def selected_broad_option(self):
        return self._selected_broad_option
        
    @property
    def selected_class(self):
        return self._selected_class
        
    @property
    def classes_menu(self):
        return self._classes_menu
        
    @property
    def selected_weapon(self):
        return self._selected_weapon
        
    @property
    def weapons_menu(self):
        return self._weapons_menu
        
    @property
    def selected_weapon_type(self):
        return self._selected_weapon_type    
        
    @property
    def weapon_types_menu(self):
        return self._weapon_types_menu
        
    @property
    def submit_button(self):
        return self._submit_button
        
    @property
    def back_button(self):
        return self._back_button
        
    @property
    def quit_button(self):
        return self._quit_button
    
class Controller:
    current_submenu = None
        
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.directory_frame.tkraise()
        self.view.directory_frame.submit_button.bind('<Button-1>', self.submit_directories)
        self.view.directory_frame.quit_button.bind('<Button-1>', self.quit)
        self.view.crosshairs_frame.submit_button.bind('<Button-1>', self.submit_crosshair)
        self.view.crosshairs_frame.quit_button.bind('<Button-1>', self.quit)
        self.view.scripts_frame.submit_button.bind('<Button-1>', self.submit_apply_to)
        self.view.scripts_frame.back_button.bind('<Button-1>', self.go_back)
        self.view.scripts_frame.quit_button.bind('<Button-1>', self.quit)
        
        self.view.scripts_frame.selected_broad_option.trace("w", self.show_submenu)
        
    def submit_directories(self, event):
        crosshairs_directory = self.view.directory_frame.crosshairs_directory_entry.get()
        weapon_scripts_directory = self.view.directory_frame.scripts_directory_entry.get()
        if self.model.validate_directory(crosshairs_directory, "crosshairs directory") and self.model.validate_directory(weapon_scripts_directory, "weapon scripts directory"):
            new_crosshairs_list = self.model.generate_crosshairs_list(crosshairs_directory)
            self.update_crosshairs_menu(new_crosshairs_list)
            self.view.crosshairs_frame.tkraise()
            
            new_scripts_list = self.model.generate_weapons_list(weapon_scripts_directory)
            self.update_scripts_menu(new_scripts_list)
        else:
            messagebox.showerror("Invalid Directory Error", "One or more of your directories is invalid.")                  
            
    def update_crosshairs_menu(self, new_crosshairs_list):
        self.view.crosshairs_frame.selected_crosshair.set(new_crosshairs_list[0])
        self.view.crosshairs_frame.crosshairs_menu['menu'].delete(0, 'end')
        for crosshair in new_crosshairs_list:
            self.view.crosshairs_frame.crosshairs_menu['menu'].add_command(label=crosshair, command=tkinter._setit(self.view.crosshairs_frame.selected_crosshair, crosshair))
            
    def update_scripts_menu(self, new_scripts_list):
        self.view.scripts_frame.selected_weapon.set(new_scripts_list[0])
        self.view.scripts_frame.weapons_menu['menu'].delete(0, 'end')
        for weapon_script in new_scripts_list:
            self.view.scripts_frame.weapons_menu['menu'].add_command(label=weapon_script, command=tkinter._setit(self.view.scripts_frame.selected_weapon, weapon_script))
            
    def show_submenu(self, *args):
        if self.view.scripts_frame.selected_broad_option.get() == "Specific class":
            if Controller.current_submenu != None:
                if Controller.current_submenu != self.view.scripts_frame.classes_menu:
                    menu_to_remove = Controller.current_submenu
                    menu_to_remove.grid_remove()
                    self.view.scripts_frame.classes_menu.grid(row=1, column=4)
                    Controller.current_submenu = self.view.scripts_frame.classes_menu
            else:
                self.view.scripts_frame.classes_menu.grid(row=1, column=4)
                Controller.current_submenu = self.view.scripts_frame.classes_menu
        elif self.view.scripts_frame.selected_broad_option.get() == "Specific weapon":
            if Controller.current_submenu != None:
                if Controller.current_submenu != self.view.scripts_frame.weapons_menu:
                    menu_to_remove = Controller.current_submenu
                    menu_to_remove.grid_remove()
                    self.view.scripts_frame.weapons_menu.grid(row=1, column=4)
                    Controller.current_submenu = self.view.scripts_frame.weapons_menu
            else:
                self.view.scripts_frame.weapons_menu.grid(row=1, column=4)
                Controller.current_submenu = self.view.scripts_frame.weapons_menu
        elif self.view.scripts_frame.selected_broad_option.get() == "Specific weapon type":
            if Controller.current_submenu != None:
                if Controller.current_submenu != self.view.scripts_frame.weapon_types_menu:
                    menu_to_remove = Controller.current_submenu
                    menu_to_remove.grid_remove()
                    self.view.scripts_frame.weapon_types_menu.grid(row=1, column=4)
                    Controller.current_submenu = self.view.scripts_frame.weapon_types_menu
            else:
                self.view.scripts_frame.weapon_types_menu.grid(row=1, column=4)
                Controller.current_submenu = self.view.scripts_frame.weapon_types_menu         
        else:
            if Controller.current_submenu != None:
                    menu_to_remove = Controller.current_submenu
                    menu_to_remove.grid_remove()
                    Controller.current_submenu = None

    def submit_crosshair(self, event):
        self.view.scripts_frame.tkraise()
        
    def submit_apply_to(self, event):
        apply_to = None
        crosshair = self.view.crosshairs_frame.selected_crosshair.get()
        if Controller.current_submenu == self.view.scripts_frame.classes_menu:
            apply_to = self.view.scripts_frame.selected_class.get()
            self.model.modify_weapon_scripts(apply_to, crosshair)
        elif Controller.current_submenu == self.view.scripts_frame.weapons_menu:
            apply_to = self.view.scripts_frame.selected_weapon.get()
            self.model.modify_weapon_scripts(apply_to, crosshair)
        elif Controller.current_submenu == self.view.scripts_frame.weapon_types_menu:
            apply_to = self.view.scripts_frame.selected_weapon_type.get()
            self.model.modify_weapon_scripts(apply_to, crosshair)
        else:
            apply_to = "All classes/weapons"
            self.model.modify_weapon_scripts(apply_to, crosshair)
           
        messagebox.showinfo("Crosshair Applied", "Crosshair %s applied to %s!" %(crosshair, apply_to))
        #I need to set current_menu so I can get the option the user chose from it when they clicked submit
        #and determine what to do with that selected option from current_menu
        
    def go_back(self, event):
        self.view.crosshairs_frame.tkraise()
        
    def quit(self, event):
        self.view.destroy()
        
#the app is the sum of the model, view, and controller coming together
class App:
    model = Model()
    view = View()
    controller = Controller(model, view)
       
if __name__ == "__main__":
    app = App()
    app.view.mainloop()

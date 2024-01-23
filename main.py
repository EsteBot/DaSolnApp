from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

class Tabs(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class DaSolnApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
    
    # functions for tab1 M1V1=M2V2 tab  
    def calc_miss_quant(self):
        # exception handling for calculations
        try:
            # solve for missing variable calculation
            m1 = self.root.ids.m1_input.text
            v1 = self.root.ids.v1_input.text
            m2 = self.root.ids.m2_input.text
            v2 = self.root.ids.v2_input.text

            if m1 == '':
               v1 = float(self.root.ids.v1_input.text)
               m2 = float(self.root.ids.m2_input.text)
               v2 = float(self.root.ids.v2_input.text)

               self.root.ids.m1_input.color = [1, 0.6, 0]
               self.root.ids.m1_input.text = str('M1')
               self.root.ids.formula_numerator.color = [1, 0.6, 0]
               self.root.ids.formula_numerator.text = str(f'{m2} x {v2}')
               self.root.ids.formula_line.color = [1, 0.6, 0]
               self.root.ids.formula_line.text = 'M1 = '+str('___________')
               self.root.ids.formula_denominator.color = [1, 0.6, 0]
               self.root.ids.formula_denominator.text = str(v1)
               self.root.ids.output.color = [1, 0, 0.5]
               self.root.ids.output.text = 'Conc.1 = '+str((round((m2*v2)/v1,2)))

            elif v1 == '':
               m1 = float(self.root.ids.m1_input.text)
               m2 = float(self.root.ids.m2_input.text)
               v2 = float(self.root.ids.v2_input.text)

               self.root.ids.v1_input.color = [1, 0.6, 0]
               self.root.ids.v1_input.text = str('V1')
               self.root.ids.formula_numerator.color = [1, 0.6, 0]
               self.root.ids.formula_numerator.text = str(f'{m2} x {v2}')
               self.root.ids.formula_line.color = [1, 0.6, 0]
               self.root.ids.formula_line.text = 'V1 = '+str('___________')
               self.root.ids.formula_denominator.color = [1, 0.6, 0]
               self.root.ids.formula_denominator.text = str(m1)
               self.root.ids.output.color = [1, 0, 0.5]
               self.root.ids.output.text = 'Vol.1 = '+str((round((m2*v2)/m1,2)))+'mL'

            elif m2 == '':
               m1 = float(self.root.ids.m1_input.text)
               v1 = float(self.root.ids.v1_input.text)
               v2 = float(self.root.ids.v2_input.text)

               self.root.ids.m2_input.color = [1, 0.6, 0]
               self.root.ids.m2_input.text = str('M2')
               self.root.ids.formula_numerator.color = [1, 0.6, 0]
               self.root.ids.formula_numerator.text = str(f'{m1} x {v1}')
               self.root.ids.formula_line.color = [1, 0.6, 0]
               self.root.ids.formula_line.text = 'M2 = '+str('___________')
               self.root.ids.formula_denominator.color = [1, 0.6, 0]
               self.root.ids.formula_denominator.text = str(v2)
               self.root.ids.output.color = [1, 0, 0.5]
               self.root.ids.output.text = 'Conc.2 = '+str((round((m1*v1)/v2,2)))

            elif v2 == '':
               m1 = float(self.root.ids.m1_input.text)
               v1 = float(self.root.ids.v1_input.text)
               m2 = float(self.root.ids.m2_input.text)

               self.root.ids.v2_input.color = [1, 0.6, 0]
               self.root.ids.v2_input.text = str('V2')
               self.root.ids.formula_numerator.color = [1, 0.6, 0]
               self.root.ids.formula_numerator.text = str(f'{m1} x {v1}')
               self.root.ids.formula_line.color = [1, 0.6, 0]
               self.root.ids.formula_line.text = 'V2 = '+str('___________')
               self.root.ids.formula_denominator.color = [1, 0.6, 0]
               self.root.ids.formula_denominator.text = str(m2)
               self.root.ids.output.color = [1, 0, 0.5]
               self.root.ids.output.text = 'Vol.2 = '+str((round((m1*v1)/m2,2)))+'mL'

            elif m1 != '' and v1 != '' and m2 != '' and v2 != '':
                self.root.ids.mv_formula.text = str(' Formula:\n(M1)x(V1) = (M2)x(V2)')
                self.root.ids.output.text = str('')
                self.root.ids.input_error.color = [1, 0, 0.5]
                self.root.ids.input_error.text = str("There is no missing variable to solve for")

        # error message if coordinate inputs are not int or float numbers
        except ValueError:
            self.root.ids.mv_formula.text = str(' Formula:\n(M1)x(V1) = (M2)x(V2)')
            self.root.ids.output.text = str('')
            self.root.ids.input_error.color = [1, 0, 0.5]
            self.root.ids.input_error.text = str("Inputs must be whole numbers or decimal")

    release_count = 0
    def egg_button_on_release(self):
        if self.release_count == 0:
            self.egg_question()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer()
            self.release_count = 0
            return 

    def egg_question(self):
        self.root.ids.egg_question1.color = [1, 0, 0.5]
        self.root.ids.egg_question1.text = str("So many big answers?")


    def egg_answer(self):
        self.root.ids.egg_answer1.color = [1, 0, 0.5]
        self.root.ids.egg_answer1.text = str("So few little questions...")

    def m1v1m2v2_reset_func(self):
        self.release_count = 0
        self.root.ids.egg_question1.text = str('')
        self.root.ids.egg_answer1.text = str('')
        self.root.ids.m1_input.text = str('')
        self.root.ids.v1_input.text = str('')
        self.root.ids.m2_input.text = str('')
        self.root.ids.v2_input.text = str('')
        self.root.ids.formula_numerator.text = str('')
        self.root.ids.formula_line.text = str('')
        self.root.ids.formula_denominator.text = str('')
        self.root.ids.output.text = str('')
        self.root.ids.input_error.text = str('')

    # functions for tab2 ratio tab
    def calc_ratio_amounts(self):
        try:
            tot_vol = float(self.root.ids.end_vol_input.text)
            soln_A =  float(self.root.ids.ratio_input_A.text)
            soln_B =  float(self.root.ids.ratio_input_B.text)
            one_part = round(((tot_vol/(soln_A + soln_B))),3)
            end_soln_A = round((one_part * soln_A),3)
            end_soln_B = round((one_part * soln_B),3)
            self.root.ids.part_tot.color = 1, 0.98, 0.63
            self.root.ids.part_tot.text = str(f'Total Parts = {tot_vol}mL/({soln_A}+{soln_B})')
            self.root.ids.soln_A_output.color = 1, 0.98, 0.63
            self.root.ids.soln_A_output.text = str(f'Soln A Volume = {one_part}mL*{soln_A}')
            self.root.ids.soln_B_output.color = 1, 0.98, 0.63
            self.root.ids.soln_B_output.text = str(f'Soln B Volume = {one_part}mL*{soln_B}')
            self.root.ids.ratio_fmla.text = str('')
            self.root.ids.ratio_err_msg.text = str('')
            if tot_vol <= 0 or soln_A <= 0 or soln_B <= 0:
                self.root.ids.ratio_err_msg.color = [1, 0.98, 0.63]
                self.root.ids.ratio_err_msg.text = str("Soln value(s) must be > 0")
                self.root.ids.end_vol_input.text = str('')
                self.root.ids.ratio_input_A.text = str('')
                self.root.ids.ratio_input_B.text = str('')
                self.root.ids.soln_A_output.text = str('')
                self.root.ids.soln_B_output.text = str('')
                
        except ValueError:
            self.root.ids.ratio_err_msg.color = [1, 0.98, 0.63]
            self.root.ids.ratio_err_msg.text = str("dose and/or weight value(s) must be a numerical value")
            self.root.ids.end_vol_input.text = str('')
            self.root.ids.ratio_input_A.text = str('')
            self.root.ids.ratio_input_B.text = str('')
            self.root.ids.soln_A_output.text = str('')
            self.root.ids.soln_B_output.text = str('')


    release_count = 0
    def egg_button_on_release2(self):
        if self.release_count == 0:
            self.egg_question2()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer2()
            self.release_count = 0
            return 

    def egg_question2(self):
        self.root.ids.egg_question_text2.color = [1, 0.98, 0.63]
        self.root.ids.egg_question_text2.text = str("How did the\nbiologist impress\ntheir date?")

    def egg_answer2(self):
        self.root.ids.egg_answer_text2.color = [1, 0.98, 0.63]
        self.root.ids.egg_answer_text2.text = str("With designer\ngenes!!!")

    def ratio_reset_func(self):
        self.release_count = 0
        self.root.ids.egg_question_text2.text = str('')
        self.root.ids.egg_answer_text2.text = str('')
        self.root.ids.ratio_input_A.color =  1,1,1
        self.root.ids.ratio_input_A.text = str('')
        self.root.ids.ratio_input_B.color =  1,1,1
        self.root.ids.ratio_input_B.text = str('')
        self.root.ids.end_vol_input.color =  1,1,1
        self.root.ids.end_vol_input.text = str('')
        self.root.ids.soln_A_output.color =  1,1,1, 0.3
        self.root.ids.soln_A_output.text = str('Soln A Volume (mL)')
        self.root.ids.soln_B_output.color =  1,1,1, 0.3
        self.root.ids.soln_B_output.text = str('Soln B Volume (mL')
        self.root.ids.ratio_err_msg.text = str('')

    # functions for tab3 grams & Percent Soln tab
    def calc_gram_amount(self):
        try:
            end_vol = float(self.root.ids.final_vol_input.text)
            pct_sol = float(self.root.ids.pct_input.text)
            grm_amt = round((((end_vol*pct_sol)/100)),3)
            self.root.ids.calc_display.color = 0, 0.4, 1
            self.root.ids.calc_display.text = str(f'grams = ({pct_sol} * {end_vol}) / 100')
            self.root.ids.gram_output.color = 0, 0.4, 1
            self.root.ids.gram_output.text = str(f'Chemical weight needed = {grm_amt} grams')
            self.root.ids.ratio_err_msg.text = str("")
            if end_vol <= 0 or pct_sol <= 0:
                self.root.ids.gram_err_msg.color = [0, 0.4, 1]
                self.root.ids.gram_err_msg.text = str("Vol and/or Percent value(s) must be > 0")
                self.root.ids.calc_display.text = str('')
                self.root.ids.gram_output.text = str('')
                
        except ValueError:
            self.root.ids.gram_err_msg.color = [0, 0.4, 1]
            self.root.ids.gram_err_msg.text = str("dose and/or weight value(s) must be a numerical value")
            self.root.ids.calc_display.text = str('')
            self.root.ids.gram_output.text = str('')

    release_count = 0
    def egg_button_on_release3(self):
        if self.release_count == 0:
            self.egg_question3()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer3()
            self.release_count = 0
            return 

    def egg_question3(self):
        self.root.ids.egg_question_text3.color = [0, 0.4, 1]
        self.root.ids.egg_question_text3.text = str("How did the\nbiologist impress\ntheir date?")

    def egg_answer3(self):
        self.root.ids.egg_answer_text3.color = [0, 0.4, 1]
        self.root.ids.egg_answer_text3.text = str("With designer\ngenes!!!")

    def gram_reset_func(self):
        self.release_count = 0
        self.root.ids.egg_question_text3.text = str('')
        self.root.ids.egg_answer_text3.text = str('')
        self.root.ids.pct_input.color =  1,1,1
        self.root.ids.pct_input.text = str('')
        self.root.ids.final_vol_input.color =  1,1,1
        self.root.ids.final_vol_input.text = str('')
        self.root.ids.calc_display.color =  1,1,1, 0.3
        self.root.ids.calc_display.text = str('(Final Vol * Pct Val)/100 =\ngrams')
        self.root.ids.gram_output.color =  1,1,1, 0.3
        self.root.ids.gram_output.text = str('')
        self.root.ids.gram_err_msg.text = str('')

    # function to control switching between tabs
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = tab_text


DaSolnApp().run()
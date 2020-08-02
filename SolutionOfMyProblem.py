#!/usr/bin/env python

from manimlib.imports import *

because = 0
therefore = 1
other = 2
class problem(Scene):
    def construct(self):
        problem = TextMobject("已知$m$,$n$$(m<n)$为两个正实数, $f(x)=\\left|\\log_{2}{x}\\right|$(定义域为$[m^{2},n]$)且$f(m)=f(n)$，若$f(x)$的最大值为$2$，求$\\log_{m}{(n-2m)}$的值。").scale(0.8)
        #上色Begin
        i2 = 0
        HighLightsIndex = [2,4,6,8,17,19,27,35,38,42,44,47,49,53,55,68,70,73]
        HighLightsColors = [RED_C,RED_C,RED_C,RED_C,TEAL_C,YELLOW,YELLOW,RED_C,RED_C,TEAL_C,YELLOW,TEAL_C,YELLOW,TEAL_C,YELLOW,RED_C,RED_C,RED_C]
        for i in HighLightsIndex:
           problem[0][i].set_color(HighLightsColors[i2])
           i2+=1
        #上色End
        self.play(Write(problem))
        self.wait()
        self.play(problem.to_edge, UP,run_time=0.5)
        line = Line(start=LEFT*6.5,end=RIGHT*6.5).shift(UP*2.4).set_color(BLUE)
        self.play(ShowCreation(line),run_time=0.5)
        #Proof Begin
        
        MostImportantThing = TextMobject("解:").move_to(LEFT*6.2+UP*1.9)
        self.play(Write(MostImportantThing))
        
        # mp = NumberPlane().add_coordinates()
        # self.add(mp)
        
        Proofs = TextMobject(
            "$\\because f(m) = f(n)$\\\\",
            "又$\\because m < n$\\\\",
            "$\\therefore 0 < m < 1 <n,m = \\frac{1}{n}$\\\\",
            "$\\therefore m^{2} < m < 1$\\\\",
            "设$g(x)=\\log_{2}{x}(m^{2}\\le x \\le n)$\\\\",
            "$\\because \\log_{2}{x}$的底数$2>1$\\\\",
            "$\\therefore g(x)$在$[m^{2},n]$上为增函数\\\\",
            "$\\therefore g(m^{2}) < g(m)$\\\\",
            "$\\therefore -g(m^{2}) >-g(m)$\\\\",
            "$\\because -g(m)=g(\\frac{1}{m})=g(n)$\\\\",
            "$\\therefore -g(m^{2})>g(n)$\\\\",
            "$\\because f(m^{2})=-g(m^{2}),f(n)=g(n)$\\\\"
            #TODO
        ).scale(0.7).shift(DOWN*1.2)
        Proofs2 = TextMobject(
            "$\\therefore f(m^{2})>f(n)$\\\\",
            "$\\therefore f(x)_{max}=f(m^{2})=\\left|\\log_{2}{m^{2}}\\right|=-\\log_{2}{m^{2}}=2$\\\\",
            "$\\therefore m^{2} = \\frac{1}{4}$\\\\",
            "$\\therefore m = \\frac{1}{2}$,$n=2$\\\\",
            "$\\therefore \\log_{m}{(n-2m)} = \\log_{\\frac{1}{2}}{(2-2 \\times \\frac{1}{2})}=\\log_{\\frac{1}{2}}{1}=0$"
            ).scale(0.7).shift(RIGHT*2.7+UP*0.4)
        TypeOfEachProofs = [because,because,therefore,therefore,other,because,therefore,therefore,therefore,because,therefore,because,therefore,therefore,therefore,therefore,therefore]
        funcGgraphy = FunctionGraph(lambda x:np.log2(x),x_min = 0.12,x_max=5)
        axe2 = Axes(
            x_min=-1,y_min=-3,
            x_max=5 ,y_max= 3
        )
        fxgp = VGroup(Proofs[5][1:6])
        axe2.add_coordinates()
        grp1 = VGroup(axe2,funcGgraphy).scale(0.5).shift(RIGHT*2+DOWN*1.2)

        maxproofs = Proofs.__len__()
        maxlength = 0
        maxlengthindex = 0
        #proof1
        for i in range(0,maxproofs):
            if Proofs[i].__len__() > maxlength:
                maxlength = Proofs[i].__len__()
                maxlengthindex = i
            #begin 对齐
        for i in range(0,maxproofs):
            Proofs[i].align_to(Proofs[maxlengthindex],LEFT)
            #end 对齐
        #proof1 end
        #proof2 begin
        maxproofs = Proofs2.__len__();
        maxlength = 0
        maxlengthindex = 0
        for i in range(0,maxproofs):
            if Proofs2[i].__len__() > maxlength:
                maxlength = Proofs2[i].__len__()
                maxlengthindex = i
            #begin 对齐
        for i in range(0,maxproofs):
            Proofs2[i].align_to(Proofs2[maxlengthindex],LEFT)
        #proof2 end
        gp = VGroup()
        maxproofs = Proofs.__len__()
        for i in range(0,maxproofs):
            if TypeOfEachProofs[i] == therefore:
               self.play(TransformFromCopy(gp,Proofs[i]))
               if TypeOfEachProofs[i-1] != because:
                   gp = VGroup()
            else:
               self.play(Write(Proofs[i]))
               gp.add(Proofs[i])
            if i == 6:
                self.play(ShowCreationThenDestructionAround(fxgp))
                self.play(TransformFromCopy(fxgp,axe2))
                self.play(ShowCreation(funcGgraphy),run_time = 0.5)
            self.wait()
        self.play(Proofs.move_to,LEFT*4+DOWN*1.2,grp1.move_to,np.array([0.7,-2.3,0]))
        #self.play(Uncreate(Proofs))
        gp = VGroup()
        maxproofs = Proofs2.__len__()
        for i in range(0,maxproofs):
            if TypeOfEachProofs[i] == therefore:
                self.play(TransformFromCopy(gp,Proofs2[i]))
                if TypeOfEachProofs[i-1] != because:
                   gp = VGroup()
            else:
                self.play(Write(Proofs2[i]))
                gp.add(Proofs2[i])
            self.wait()
        axe1 = Axes(
            x_min=-1,y_min=-1,
            x_max=5 ,y_max= 5,
            center_poin=RIGHT*1+DOWN*4
        )
        fxgp = VGroup(problem[0][17:29])
        self.play(ShowCreationThenDestructionAround(fxgp))
        axe1.add_coordinates()
        func1 = FunctionGraph(lambda t: np.abs(np.log2(t)),x_max=5,x_min=0.1)
        grp = VGroup(axe1,func1).scale(0.5).shift(RIGHT*2.6+DOWN*4.2)
        self.play(TransformFromCopy(fxgp,axe1))
        self.play(ShowCreation(func1))
        self.wait(4)
        self.play(FadeOut(problem),FadeOut(line),FadeOut(MostImportantThing),FadeOut(Proofs),FadeOut(Proofs2),FadeOut(axe1),FadeOut(func1),FadeOut(grp1))
        #Proof End
        end = TextMobject("Made by Cai1Hsu with ","Manim")
        end[1].set_color_by_gradient("#58C4DD","#8B4513")
        self.play(FadeIn(end))
        self.wait()
        self.play(Uncreate(end))


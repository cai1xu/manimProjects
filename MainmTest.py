#!/usr/bin/env python

from manimlib.imports import *

# See old_projects folder for many, many more
#Proof that \log_{a}{b} \times \log_{b}{c} \times \log_{c}{a}=1
class MathExample(Scene):
    def construct(self):
        problem = TextMobject("已知$\\log_{a}{b}=\\frac{\\log_{c}{b}}{\\log_{c}{a}}$(换底公式),\\\请证明 $\\log_{a}{b} \\times \\log_{b}{c} \\times \\log_{c}{a}=1$.")
        self.play(Write(problem))
        self.wait(2)
        source = TextMobject("原式","=$\\log_{a}{b} \\times \\log_{b}{c} \\times \\log_{c}{a}$","\\\=$\\frac{\\log_{\\pi}{b}}{\\log_{\\pi}{a}} \\times \\frac{\\log_{\\pi}{c}}{\\log_{\\pi}{b}} \\times \\frac{\\log_{\\pi}{a}}{\\log_{\\pi}{c}}$","\\\=$1\\times 1 \\times\\ 1$","\\\=$1$")
        source[2].align_to(source[1],LEFT)
        source[3].align_to(source[1],LEFT)
        source[4].align_to(source[1],LEFT)
        self.play(Transform(problem,source[0]))
        self.play(Write(source[1]))
        self.wait(1)
        self.play(TransformFromCopy(source[1],source[2]))
        self.wait(1)
        gp1 = VGroup(source[2][1:6])
        gp2 = VGroup(source[2][13:18])
        gp3 = VGroup(source[2][7:12])
        gp4 = VGroup(source[2][31:36])
        self.play(Swap(gp1,gp2))
        self.play(Swap(gp3,gp4))
        self.wait()
        self.play(Write(source[3][0]))
        self.play(TransformFromCopy(VGroup(gp2,gp4,source[2][6]),source[3][1]))
        self.play(Write(source[3][2]))
        self.play(TransformFromCopy(VGroup(gp1,source[2][18:24]),source[3][3]))
        self.play(Write(source[3][4]))
        self.play(TransformFromCopy(VGroup(source[2][25:31],gp3),source[3][5]))
        self.play(TransformFromCopy(source[3],source[4]))
        self.wait(3)
        self.play(FadeOut(problem),FadeOut(source))
        end = TextMobject("Made by Cai1Hsu with ","Manim")
        end[1].set_color_by_gradient("#58C4DD","#8B4513")
        self.play(FadeIn(end))
        self.wait()
        self.play(Uncreate(end))



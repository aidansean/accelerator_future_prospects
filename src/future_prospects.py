import ROOT
import array

##########################################################################################
#                                    Physical values                                     #
##########################################################################################
# Fix these up as we get better measurements :)
higgs_mass  = 125
higgs_width = 4.0

# CMS limit on the Higgs width
higgs_width_CMS = 22.0

##########################################################################################
#                                 Class to handle points                                 #
##########################################################################################
class collider_point:
    def __init__(self, name, energy, lumi, mH, GH, color, marker):
        self.name   = name
        self.energy = energy
        self.lumi   = lumi
        self.mH     = mH
        self.GH     = GH*higgs_width/100
        x = array.array('d')
        y = array.array('d')
        x.append(self.mH)
        y.append(self.GH)
        self.graph = ROOT.TGraph(1, x, y)
        
        self.graph.SetMarkerColor(color )
        self.graph.SetMarkerStyle(marker)
        self.graph.SetMarkerSize(4)
        self.graph.SetTitle('a simple graph')
        self.graph.GetXaxis().SetTitle('m_{H} resolution [GeV]')
        self.graph.GetYaxis().SetTitle('#Gamma_{H} resolution [%]')
        
        text_x = self.mH
        latex_text = '#splitline{%s}{(%s, %s fb^{-1})}'%(self.name, self.energy, self.lumi)
        latex_text = '%s  '%self.name
        self.label = ROOT.TLatex(text_x, self.GH, latex_text)
        self.label.SetTextAlign(32)
        self.label.SetTextSize(0.03)
        
        if self.name=='Whitespace':
            self.graph.SetMarkerSize(0)

##########################################################################################
#                                  Input the data here                                   #
##########################################################################################
LHC_markerStyle = 20
ILC_markerStyle = 21

collider_points = []
collider_points.append( collider_point('Whitespace'  , ''                 , ''              , 600, 100*5000/4, ROOT.kWhite , 0             ) )

collider_points.append( collider_point('LHC Run 1'   , '7/8 TeV'          , '~25'           , 400, 100*2600/4, ROOT.kRed+2, LHC_markerStyle) )
collider_points.append( collider_point('LHC Runs 1-3', '7/8/14 TeV'       , '300'           , 100,   100*70/4, ROOT.kRed-6, LHC_markerStyle) )
collider_points.append( collider_point('LHC Runs 1-6', '7/8/14 TeV'       , '3000'          ,  50,   100*25/4, ROOT.kRed-9, LHC_markerStyle) )

collider_points.append( collider_point('#muC'        , '126 GeV'          , '4.2'           , 0.06,  4.3, ROOT.kOrange-2, 22               ) )

collider_points.append( collider_point('CLIC'       , '350/1400/3000 GeV' , '500+1500+2000' ,   33,  8.4, ROOT.kGreen-2  , 23              ) )
#collider_points.append( collider_point('ILC 500'    , '250/500 GeV'      , '250+500'       ,   32,  5.0, ROOT.kRed+2    , ILC_markerStyle ) )
collider_points.append( collider_point('ILC 1000'    , '250/500/1000 GeV' , '250+500+1000'  ,   32,  4.6, ROOT.kBlue-9   , ILC_markerStyle ) )
collider_points.append( collider_point('ILC 1000-up' , '250/500/1000 GeV' , '1150+1600+2500',   15,  2.5, ROOT.kBlue-3   , ILC_markerStyle ) )
collider_points.append( collider_point('TLEP (4-IP)' , '240/350 GeV'      , '10000+2600'    ,    7,  1.0, ROOT.kMagenta+1, 33              ) )

collider_points.append( collider_point('Whitespace'  , ''                 , ''              , 0.02,  0.9, ROOT.kWhite    ,              0  ) )

##########################################################################################
#                                    Set ROOT styles                                     #
##########################################################################################
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
#ROOT.gStyle.SetFillStyle(ROOT.kWhite)
ROOT.gStyle.SetOptTitle(0)
ROOT.gStyle.SetFrameBorderMode(ROOT.kWhite)
ROOT.gStyle.SetFrameFillColor(ROOT.kWhite)
ROOT.gStyle.SetCanvasBorderMode(ROOT.kWhite)
ROOT.gStyle.SetCanvasColor(ROOT.kWhite)
ROOT.gStyle.SetPadBorderMode(ROOT.kWhite)
ROOT.gStyle.SetPadColor(ROOT.kWhite)
ROOT.gStyle.SetStatColor(ROOT.kWhite)
ROOT.gStyle.SetErrorX(0)

##########################################################################################
#                                     Create canvas                                      #
##########################################################################################
canvas = ROOT.TCanvas('canvas', '', 100, 100, 2000, 1200)
canvas.SetLogx()
canvas.SetLogy()
canvas.SetGridx()
canvas.SetGridy()

##########################################################################################
#                                Add points to multigraph                                #
##########################################################################################
mg = ROOT.TMultiGraph('mg_colliders', '')
for cp in collider_points:
    mg.Add(cp.graph)

# We must draw the multigraph before we can change the axes properties
mg.Draw('AP')
mg.GetXaxis().SetTitle('m_{H} resolution [MeV]')
mg.GetYaxis().SetTitle('#Gamma_{H} resolution [MeV]')
mg.GetXaxis().SetTitleOffset(1.25)
mg.GetYaxis().SetTitleOffset(1.25)

##########################################################################################
#                                 Make Higgs width lines                                 #
##########################################################################################
# These mark the SM Higgs width and the limits from eg CMS, ATLAS
# This must be done after we know the extent of the multigraph space

# line_scale_factor is used to position the label
line_scale_factor = 0.6

# Higgs width
width_line_100 = ROOT.TLine(mg.GetXaxis().GetXmin(), higgs_width, mg.GetXaxis().GetXmax(), higgs_width)
width_line_100.SetLineWidth(2)
width_line_100.SetLineColor(ROOT.kRed)

width_text_100 = ROOT.TLatex(mg.GetXaxis().GetXmin()*1.25, higgs_width*line_scale_factor, '#Gamma_{H} = 4 MeV (m_{H} = 125 GeV)')
width_text_100.SetTextSize(0.025)

# Limit from CMS
width_line_CMS = ROOT.TLine(mg.GetXaxis().GetXmin(), higgs_width_CMS, mg.GetXaxis().GetXmax(), higgs_width_CMS)
width_line_CMS.SetLineWidth(2)
width_line_CMS.SetLineColor(ROOT.kBlue)
width_line_CMS.SetLineStyle(ROOT.kDashed)

width_text_CMS = ROOT.TLatex(mg.GetXaxis().GetXmin()*1.25, higgs_width_CMS*line_scale_factor, '#Gamma_{H} < 22 MeV (CMS, arXiV:1407.0558 [hep-ex])')
width_text_CMS.SetTextSize(0.025)


##########################################################################################
#                                      Create legend                                     #
##########################################################################################
# For very long legend information you may want to split the information over two entries
single_legend_row_per_entry = True
legend = ROOT.TLegend(0.12,0.88,0.50,0.58)
legend.SetFillColor(ROOT.kWhite)
legend.SetBorderSize(0)
legend.SetShadowColor(0)
hBlank = ROOT.TH1F('hBlank', '', 100, 0, 1)
for cp in collider_points:
    if cp.name=='Whitespace':
        continue
    if single_legend_row_per_entry:
        entry_text = '%s (#sqrt{s} = %s, L = %s fb^{-1}'%(cp.name, cp.energy, cp.lumi)
        legend.AddEntry(cp.graph, entry_text, 'p')
    else:
        entry_text = '%s (#sqrt{s} = %s,'%(cp.name, cp.energy)
        legend.AddEntry(cp.graph, entry_text, 'p')
        entry_text = '  L = %s fb^{-1})'%(cp.lumi)
        legend.AddEntry(hBlank, entry_text, '')
        
##########################################################################################
#                                     Draw everything                                    #
##########################################################################################
mg.Draw('AP')
for cp in collider_points:
    if cp.name=='Whitespace':
        continue
    cp.label.Draw()

width_line_100.Draw()
width_text_100.Draw()

width_line_CMS.Draw()
width_text_CMS.Draw()

legend.Draw()

##########################################################################################
#                                      Print canvas                                      #
##########################################################################################
canvas.Print('colliders.eps')
canvas.Print('colliders.png')

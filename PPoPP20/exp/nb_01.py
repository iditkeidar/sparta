
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/01_graphs.ipynb

from exp.nb_00 import *

# average latency, 12 threads, Clueweb
def avg_latency_clueweb():
    # 1-12 terms, 12 threads, NRA, RA and parallel BMW (non-safe)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y3 = [2, 10, 26, 41, 67, 138, 161, 241, 248, 288, 366, 414]
    #y3 = [2, 22, 40, 46, 61, 102, 119, 161, 165, 168, 216, 256]
    y1 = [8, 20, 27, 38, 58, 89, 113, 152, 153, 156, 165, 177]
    y2 = [18, 43, 59, 91, 128, 172, 245, 327, 379, 472, 551, 630]
    y5 = [8, 32, 66, 104, 171, 255, 384, 577, 675, 797, 1010, 1096]
    y4 = [60, 83, 178, 236, 437, 558, 600, 716, 777, 770, 871, 965]
    y6 = [15, 112, 257, 476, 674, 916, 1180, 1447, 1458, 1688, 1881, 1922]

    ymin = 0
    xmin = 0
    ylim = 2000
    xlim = 12
    legend_loc = 2
    yscale = 'linear'
    y3_name = 'pRA - high'
    y1_name = 'Sparta - high'
    y2_name = 'pBMW - high'
    y5_name = 'pJASS - high'
    y4_name = 'pNRA - high'
    y6_name = 'sNRA - high'

    y4_marker = 'h'
    y2_marker = 'o'
    y3_marker = 's'
    y1_marker = 'h'
    y5_marker = 'v'
    y6_marker = 'h'

    y4_color = 4
    y2_color = 0
    y3_color = 5
    y1_color = 8
    y5_color = 2
    y6_color = 10

    draw_chart_6_new_new(x, y1, y1_name, y1_marker, y1_color, y2, y2_name, y2_marker, y2_color, y3, y3_name, y3_marker, y3_color, y4, y4_name, y4_marker, y4_color, y5, y5_name, y5_marker, y5_color, y6, y6_name, y6_marker, y6_color, "terms",
                     "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_12threads_clueweb")

# avg_latency_clueweb()

# 95th percentile latency, 12 threads, Clueweb
def perc_95_clueweb():
    # 1-12 terms, 12 threads, NRA, RA and parallel BMW (non-safe)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y3 = [12, 151, 237, 393, 405, 481, 547, 727, 663, 641, 1054, 1075]
    y1 = [16, 83, 337, 342, 354, 367, 377, 378, 390, 398, 437, 495]
    y2 = [165, 200, 253, 299, 292, 411, 494, 608, 701, 859, 1090, 1160]
    y5 = [35, 129, 315, 346, 532, 608, 1014, 1410, 1598, 1754, 2064, 2933]
    y4 = [262, 305, 445, 526, 898, 1009, 1103, 1226, 1263, 1367, 1587, 1605]
    y6 = [31, 382, 660, 1177, 1355, 1832, 2063, 2595, 2553, 2835, 3066, 3286]

    ymin = 0
    xmin = 0
    ylim = 3400
    xlim = 12
    legend_loc = 2
    yscale = 'linear'
    y3_name = 'pRA - high'
    y1_name = 'Sparta - high'
    y2_name = 'pBMW - high'
    y5_name = 'pJASS - high'
    y4_name = 'pNRA - high'
    y6_name = "sNRA - high"

    y4_marker = 'h'
    y2_marker = 'o'
    y3_marker = 's'
    y1_marker = 'h'
    y5_marker = 'v'
    y6_marker = 'h'

    y4_color = 4
    y2_color = 0
    y3_color = 5
    y1_color = 8
    y5_color = 2
    y6_color = 10

    #draw_chart_5_new(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, "terms", "latency (ms)", xmin, ymin, xlim,ylim, yscale, legend_loc, "latency_95th_percentile_clueweb")
    #draw_chart_6_new(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, y6, y6_name, "terms", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_95th_percentile_clueweb")
    draw_chart_6_new_new(x, y1, y1_name, y1_marker, y1_color, y2, y2_name, y2_marker, y2_color, y3, y3_name, y3_marker,
                         y3_color, y4, y4_name, y4_marker, y4_color, y5, y5_name, y5_marker, y5_color, y6, y6_name,
                         y6_marker, y6_color, "terms",
                         "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_95th_percentile_clueweb")
# perc_95_clueweb()

# average latency, 12 threads, Clueweb
def avg_latency_12t_clueweb():
    # 1-12 terms, 12 threads, NRA, RA and parallel BMW (non-safe)
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #y2 = [18, 43, 59, 91, 128, 172, 245, 327, 379, 472, 551, 630]
    y3 = [19, 39, 58, 94, 117, 148, 209, 293, 325, 401, 469, 536]
    #y5 = [8, 32, 66, 104, 171, 255, 384, 577, 675, 797, 1010, 1096]
    y2 = [3, 14, 34, 58, 78, 101, 137, 190, 206, 256, 278, 292]
    y1 = [8, 20, 27, 38, 58, 89, 113, 152, 153, 156, 165, 177]

    ymin = 0
    xmin = 0
    ylim = 600
    xlim = 12
    legend_loc = 2
    yscale = 'linear'
    #y2_name = 'pBMW - high'
    y3_name = 'pBMW - low'
    #y5_name = 'pJASS - high'
    y2_name = 'pJASS - low'
    y1_name = 'Sparta - high'

    y2_marker = 'v'
    y1_marker = 'h'
    y3_marker = 'o'

    y2_color = 1
    y1_color = 8
    y3_color = 6

    # draw_chart_5_new(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, "terms", "latency (ms)", xmin, ymin, xlim,ylim, yscale, legend_loc, "latency_12threads_clueweb")
    #draw_chart_5_new(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, "terms", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_high_low_12threads_clueweb")
    draw_chart_3_new_new(x, y1, y1_name, y1_marker, y1_color, y2, y2_name, y2_marker, y2_color, y3, y3_name, y3_marker, y3_color,
                         "terms", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_high_low_12threads_clueweb")
# avg_latency_12t_clueweb()

# 95th percentile, 12 threads, Clueweb
def perc_95_12t_clueweb():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #y5 = [35, 129, 315, 346, 532, 608, 1014, 1410, 1598, 1754, 2064, 2933]
    y1 = [16, 83, 337, 342, 354, 367, 377, 378, 390, 398, 437, 495]
    #y2 = [165, 200, 253, 299, 292, 411, 494, 608, 701, 859, 1090, 1160]
    y3 = [57, 81, 142, 207, 264, 378, 439, 619, 602, 762, 939, 1151]
    y2 = [20, 47, 91, 135, 153, 195, 301, 376, 438, 525, 623, 654]

    ymin = 0
    xmin = 0
    ylim = 1200
    xlim = 12
    legend_loc = 2
    yscale = 'linear'
    #y5_name = 'pJASS - high'
    y1_name = 'Sparta - high'
    #y2_name = 'pBMW - high'
    y3_name = 'pBMW - low'
    y2_name = 'pJASS - low'

    y2_marker = 'v'
    y1_marker = 'h'
    y3_marker = 'o'

    y2_color = 1
    y1_color = 8
    y3_color = 6



    # draw_chart_5_new(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, "terms", "latency (ms)", xmin, ymin, xlim,ylim, yscale, legend_loc, "latency_95th_percentile_clueweb")
    #draw_chart_5_new(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, "terms", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_95th_percentile_high_low_clueweb")
    draw_chart_3_new_new(x, y1, y1_name, y1_marker, y1_color, y2, y2_name, y2_marker, y2_color, y3, y3_name, y3_marker,
                         y3_color,
                         "terms", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc,
                         "latency_95th_percentile_high_low_clueweb")
# perc_95_12t_clueweb()

# average latency, 12 threads, Clueweb_X10
def avg_latency_12t_clueweb_x10():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y3 = [9, 119, 346, 615, 944, 1169, 1437, 1669, 1713, 2048, 2053, 2065]
    y4 = [28, 68, 80, 100, 104, 106, 106, 108, 112, 115, 118, 143]
    # y1 = [77, 236, 485, 1157, 1933, 2768, 4290, 5720, 6585, 8259, 9009, 9915]
    y2 = [107, 192, 434, 1019, 1782, 2466, 3790, 5091, 6095, 7727, 8490, 9035]
    y5 = [87, 227, 397, 458, 619, 714, 802, 852, 908, 1018, 1046, 1118]
    y6 = [19, 79, 236, 308, 820, 925, 1212, 1433, 2039, 2403, 2483, 2984]
    y1 = [110.28, 771.15, 1798.85, 2979.3, 5618.99, 8833.22, 15444.35, 24626.66, 28296.02, 33969.86, 43178.91, 48732.38]

    ymin = 0
    xmin = 0
    ylim = 5000
    xlim = 12
    legend_loc = 2
    yscale = 'linear'
    y3_name = 'pRA - high'
    y4_name = 'Sparta - high'
    y1_name = 'pJASS - low'
    y2_name = 'pBMW - low'
    y5_name = 'pNRA - high'
    y6_name = 'sNRA - high'
    y7_name = 'pJass - low'


    #draw_chart_5_new(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, "terms", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_12threads_cluewebX10")
    draw_chart_6_new(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, y6, y6_name, "terms", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_12threads_cluewebX10")

# avg_latency_12t_clueweb_x10()

# 1-12 threads, 12 terms, Clueweb
def scaling_12terms_clueweb():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y3 = [1569, 1208, 896, 685, 595, 481, 437, 431, 425, 420, 416, 414]
    y1 = [840, 444, 402, 358, 321, 307, 283, 255, 228, 201, 183, 177]
    y4 = [3916, 2073, 1454, 1151, 967, 833, 767, 695, 667, 651, 639, 630]
    #y2 = [3527, 1882, 1326, 1052, 885, 772, 676, 630, 578, 546, 518, 502]
    y2 = [2063, 1329, 1162, 1115, 1111, 1098, 1070, 1056, 1048, 1039, 1027, 1096]
    ymin = 0
    xmin = 0
    ylim = 3930
    xlim = 12
    legend_loc = 1
    yscale = 'linear'
    y3_name = 'pRA - high'
    y1_name = 'Sparta - high'
    y4_name = 'pBMW - high'
    #y2_name = 'pBMW - low'
    y2_name = 'pJASS - high'

    y4_marker = 'o'
    y2_marker = 'v'
    y3_marker = 's'
    y1_marker = 'h'

    y4_color = 0
    y2_color = 2
    y3_color = 5
    y1_color = 8

    #draw_chart_4(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, "parallelism (threads)", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_12terms_clueweb")
    draw_chart_4_new_new(x, y1, y1_name, y1_marker, y1_color, y2, y2_name, y2_marker, y2_color, y3, y3_name, y3_marker,
                         y3_color, y4, y4_name, y4_marker, y4_color,
                         "parallelism (threads)", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc,
                         "latency_12terms_clueweb")

# scaling_12terms_clueweb()

# 1-12 threads, 12 terms, Clueweb_x10
def scaling_12terms_clueweb_x10():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y3 = [7055, 5924, 5396, 5096, 4888, 4584, 4336, 4008, 3567, 2987, 2571, 2065]
    y4 = [711, 404, 363, 312, 285, 267, 241, 212, 189, 166, 146, 143]
    y1 = [48377, 38153, 27626, 22286, 18472, 15859, 14323, 12943, 12164, 11209, 10850, 9915]
    # y2 = [40544, 31808, 23686, 19161, 16045, 13668, 12764, 11456, 10711, 10235, 9577, 9389]
    y2 = [110647.37, 62056.1, 51735.3, 48605.63, 45680.32, 47602.8, 47449.48, 49979.6, 51167.35, 49864.29, 50421.31, 49212.29]
    ymin = 0
    xmin = 0
    ylim = 60000
    xlim = 12
    legend_loc = 5
    yscale = 'linear'
    y3_name = 'pRA - high'
    y4_name = 'Sparta - high'
    y1_name = 'pBMW - high'
    y2_name = 'pJASS - low'

    draw_chart_4(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, "parallelism (threads)", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_12terms_cluewebX10")
    # draw_chart_2(x, y3, y3_name, y4, y4_name, "parallelism (threads)", "latency (ms)", xmin, ymin, xlim, ylim, yscale, legend_loc, "latency_12terms_cluewebX10")

# scaling_12terms_clueweb_x10()

# cumulative doc inserts, Clueweb: 12 terms, 12 threads, NRA, RA, Jass and parallel BMW (f=1,5,10)
def recall_dynamycs_clueweb():
    x = [0, 20, 40, 60, 80, 100, 130, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    y3 = [0, 25, 45, 65, 85, 86, 87, 89, 90, 92, 93, 93.5, 94, 94.25, 94.5, 94.75, 95, 95.25, 95.5, 95.75, 95.8, 96, 96, 96, 96]
    y4 = [0, 0, 0.1, 1, 2.7, 5.3, 10.7, 15.5, 33.5, 55.1, 84, 99.6, 100, 100, None, None, None, None, None, None, None, None, None, None, None]
    y1 = [0, 42.1, 75, 87.1, 91.2, 93.2, 95, 95.9, 97.8, 99, 99.5, 99.7, 99.8, 99.9, 99.9, 100, 100, 100, 100, 100, 100, 100, None, None, None]
    y2 = [0, 0, 0, 0.1, 0.5, 1.1, 2.9, 3.8, 8.2, 13.6, 19.6, 27.5, 36.4, 44.9, 54, 65.6, 80, 92.7, 98.4, 100, None, None, None, None, None]
    y5 = [0, 0, 0.5, 2.4, 4.4, 6.8, 10.7, 12.9, 20.1, 29.5, 40.6, 51.2, 65.2, 82.8, 94.2, 95, None, None, None, None, None, None, None, None, None]
    y6 = [0, 0.1, 1.4, 3.2, 4.8, 7.1, 11.2, 13.8, 21.9, 32.8, 45.4, 60, 71.7, 76.1, None, None, None, None, None, None, None, None, None, None, None]
    ymin = 0
    xmin = 0
    ylim = 100
    xlim = 1000
    legend_loc = 4
    yscale = 'linear'
    y4_name = 'pRA - exact'
    y1_name = 'Sparta - exact'
    y2_name = 'pBMW - exact'
    y5_name = 'pBMW - high'
    y6_name = 'pBMW - low'
    y3_name = 'pJASS - exact'

    y2_marker = 'o'
    y1_marker = 'h'
    y5_marker = 'o'
    y6_marker = 'o'
    y3_marker = 'v'
    y4_marker = 's'


    y2_color = 3
    y1_color = 7
    y3_color = 9
    y5_color = 0
    y6_color = 6
    y4_color = 11


    #draw_chart_5(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, "running time (ms)", "recall (%)", xmin, ymin, xlim, ylim, yscale, legend_loc, "cumulative_12threads_clueweb")
    draw_chart_6_new_new(x, y1, y1_name, y1_marker, y1_color, y2, y2_name, y2_marker, y2_color, y3, y3_name, y3_marker,
                         y3_color, y4, y4_name, y4_marker, y4_color, y5, y5_name, y5_marker, y5_color, y6, y6_name, y6_marker, y6_color,
                         "running time (ms)", "recall (%)", xmin, ymin, xlim, ylim, yscale, legend_loc, "cumulative_12threads_clueweb")
# recall_dynamycs_clueweb()

# cumulative doc inserts, Clueweb_X10: 12 terms, 12 threads, NRA, RA and parallel BMW (f=1 ,5,10)
def recall_dynamics_clueweb_x10():
    x = [0, 30, 60, 90, 120, 150, 250, 350, 500, 1000, 2000, 3000, 3250, 3600, 5970, 6940, 7410, 10210, 12000]
    y1 = [0, 56.8, 87.8, 92.2, 93.9, 94.9, 96.5, 97.5, 98.1, 98.9, 99.4, 99.6, 99.6, 99.7, 99.9, 99.9, 99.9, 100, 100]
    y2 = [0, 0, 0, 0, 0, 0, 0, 0.1, 0.4, 2.7, 9.5, 19.3, 21.4, 24.4, 52.3, 67.4, 73.4, 100, None]
    y3 = [0.0, 26.708999999999996, 58.483000000000004, 79.4, 89.602, 89.904, 90.444, 90.878, 91.297, 92.106, 93.33099999999999, 94.161, 94.384, 94.643, 95.94, 96.342, 96.482, 97.147, 97.416]
    #pJass here
    y4 = [0, 0, 0, 0, 0, 0, 0.5, 1.3, 2.5, 13.2, 53.9, 90.1, 95, 99.2, 100, 100, 100, None, None]
    y5 = [0, 0, 0, 0, 0.1, 0.2, 1, 2.2, 3.4, 10, 26.8, 42.5, 46.3, 51.5, 87.4, 96.9, None, None, None]
    y6 = [0, 0, 0, 0, 0, 0, 0.5, 1.1, 3.1, 9.2, 24.8, 38.5, 42.1, 47.3, 78.7, None, None, None, None]

    # ymin = 0
    # xmin = 0
    # ylim = 100
    # xlim = 13000
    # legend_loc = 4
    # yscale = 'linear'
    # y4_name = 'pRA - exact'
    # y5_name = 'Sparta - exact'
    # y1_name = 'pBMW - exact'
    # y2_name = 'pBMW - high'
    # y3_name = 'pBMW - low'

    # draw_chart_5(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, "running time (ms)", "recall (%)", xmin, ymin, xlim, ylim, yscale, legend_loc, "cumulative_12threads_cluewebX10")


    ymin = 0
    xmin = 0
    ylim = 100
    xlim = 12000
    legend_loc = 4
    yscale = 'linear'
    y4_name = 'pRA - exact'
    y1_name = 'Sparta - exact'
    y2_name = 'pBMW - exact'
    y5_name = 'pBMW - high'
    y6_name = 'pBMW - low'
    y3_name = 'pJASS - exact'

    y2_marker = 'o'
    y1_marker = 'h'
    y5_marker = 'o'
    y6_marker = 'o'
    y3_marker = 'v'
    y4_marker = 's'


    y2_color = 3
    y1_color = 7
    y3_color = 9
    y5_color = 0
    y6_color = 6
    y4_color = 11


    #draw_chart_5(x, y1, y1_name, y2, y2_name, y3, y3_name, y4, y4_name, y5, y5_name, "running time (ms)", "recall (%)", xmin, ymin, xlim, ylim, yscale, legend_loc, "cumulative_12threads_clueweb")
    draw_chart_6_new_new(x, y1, y1_name, y1_marker, y1_color, y2, y2_name, y2_marker, y2_color, y3, y3_name, y3_marker,
                         y3_color, y4, y4_name, y4_marker, y4_color, y5, y5_name, y5_marker, y5_color, y6, y6_name, y6_marker, y6_color,
                         "running time (ms)", "recall (%)", xmin, ymin, xlim, ylim, yscale, legend_loc, "cumulative_12threads_clueweb")

# recall_dynamics_clueweb_x10()
def get_colors(style: str = None, names: bool = None) -> dict | list | str:    material_color = {'red':          ['#b71c1c', '#c62828', '#d32f2f', '#e53935', '#f44336', '#ef5350', '#e57373', '#ef9a9a', '#ffcdd2', '#ffebee'],                      'pink':         ['#880e4f', '#ad1457', '#c2185b', '#d81b60', '#e91e63', '#ec407a', '#f06292', '#f48fb1', '#f8bbd0', '#fce4ec'],                      'indigo':       ['#4a148c', '#6a1b9a', '#7b1fa2', '#8e24aa', '#9c27b0', '#ab47bc', '#ba68c8', '#ce93d8', '#e1bee7', '#f3e5f5'],                      'purple':       ['#311b92', '#4527a0', '#512da8', '#5e35b1', '#673ab7', '#7e57c2', '#9575cd', '#b39ddb', '#d1c4e9', '#ede7f6'],                      'dark blue':    ['#1a237e', '#283593', '#303f9f', '#3949ab', '#3f51b5', '#5c6bc0', '#7986cb', '#9fa8da', '#c5cae9', '#e8eaf6'],                      'blue':         ['#0d47a1', '#1565c0', '#1976d2', '#1e88e5', '#2196f3', '#42a5f5', '#64b5f6', '#90caf9', '#bbdefb', '#e3f2fd'],                      'blue2':        ['#01579b', '#0277bd', '#0288d1', '#039be5', '#03a9f4', '#29b6f6', '#4fc3f7', '#81d4fa', '#b3e5fc', '#e1f5fe'],                      'sea blue':     ['#006064', '#00838f', '#0097a7', '#00acc1', '#00bcd4', '#26c6da', '#4dd0e1', '#80deea', '#b2ebf2', '#e0f7fa'],                      'cyprus':       ['#004d40', '#00695c', '#00796b', '#00897b', '#009688', '#26a69a', '#4db6ac', '#80cbc4', '#b2dfdb', '#e0f2f1'],                      'green':        ['#1b5e20', '#2e7d32', '#388e3c', '#43a047', '#4caf50', '#66bb6a', '#81c784', '#a5d6a7', '#c8e6c9', '#e8f5e9'],                      'lawn green':   ['#33691e', '#558b2f', '#689f38', '#7cb342', '#8bc34a', '#9ccc65', '#aed581', '#c5e1a5', '#dcedc8', '#f1f8e9'],                      'olive green':  ['#827717', '#9e9d24', '#afb42b', '#c0ca33', '#cddc39', '#d4e157', '#dce775', '#e6ee9c', '#f0f4c3', '#f9fbe7'],                      'yellow':       ['#f57f17', '#f9a825', '#fbc02d', '#fdd835', '#ffeb3b', '#ffee58', '#fff176', '#fff59d', '#fff9c4', '#fffde7'],                      'orange':       ['#ff6f00', '#ff8f00', '#ffa000', '#ffb300', '#ffc107', '#ffca28', '#ffd54f', '#ffe082', '#ffecb3', '#fff8e1'],                      'dark orange':  ['#e65100', '#ef6c00', '#f57c00', '#fb8c00', '#ff9800', '#ffa726', '#ffb74d', '#ffcc80', '#ffe0b2', '#fff3e0'],                      'hd orange':    ['#bf360c', '#d84315', '#e64a19', '#f4511e', '#ff5722', '#ff7043', '#ff8a65', '#ffab91', '#ffccbc', '#fbe9e7'],                      'brown':        ['#3e2723', '#4e342e', '#5d4037', '#6d4c41', '#795548', '#8d6e63', '#a1887f', '#bcaaa4', '#d7ccc8', '#efebe9'],                      'black':        ['#000000', '#151515', '#1C1C1C', '#2E2E2E', '#424242', '#585858', '#6E6E6E', '#848484', '#A4A4A4', '#BDBDBD'],                      'gray':         ['#424242', '#585858', '#6E6E6E', '#848484', '#A4A4A4', '#BDBDBD', '#D8D8D8', '#E6E6E6', '#F2F2F2', '#FAFAFA'],                      'anthracite':   ['#263238', '#37474f', '#455a64', '#546e7a', '#607d8b', '#78909c', '#90a4ae', '#b0bec5', '#cfd8dc', '#eceff1']}    flat_color = {'red oxide':      ['#641e16', '#7b241c', '#922b21', '#a93226', '#c0392b', '#cd6155', '#d98880', '#e6b0aa', '#f2d7d5', '#f9ebea'],                  'lusty':          ['#78281f', '#943126', '#b03a2e', '#cb4335', '#e74c3c', '#ec7063', '#f1948a', '#f5b7b1', '#fadbd8', '#fdedec'],                  'scarlet gum':    ['#512e5f', '#633974', '#76448a', '#884ea0', '#9b59b6', '#af7ac5', '#c39bd3', '#d7bde2', '#ebdef0', '#f5eef8'],                  'scarlet gum2':   ['#4a235a', '#5b2c6f', '#6c3483', '#7d3c98', '#8e44ad', '#a569bd', '#bb8fce', '#d2b4de', '#e8daef', '#f4ecf7'],                  'astronaut blue': ['#154360', '#1a5276', '#1f618d', '#2471a3', '#2980b9', '#5499c7', '#7fb3d5', '#a9cce3', '#d4e6f1', '#eaf2f8'],                  'orient':         ['#1b4f72', '#21618c', '#2874a6', '#2e86c1', '#3498db', '#5dade2', '#85c1e9', '#aed6f1', '#d6eaf8', '#ebf5fb'],                  'watercourse':    ['#0e6251', '#117864', '#148f77', '#17a589', '#1abc9c', '#48c9b0', '#76d7c4', '#a3e4d7', '#d1f2eb', '#e8f8f5'],                  'cyprus':         ['#0b5345', '#0e6655', '#117a65', '#138d75', '#16a085', '#45b39d', '#73c6b6', '#a2d9ce', '#d0ece7', '#e8f6f3'],                  'crusoe':         ['#145a32', '#196f3d', '#1e8449', '#229954', '#27ae60', '#52be80', '#7dcea0', '#a9dfbf', '#d4efdf', '#e9f7ef'],                  'fun green':      ['#186a3b', '#1d8348', '#239b56', '#28b463', '#2ecc71', '#58d68d', '#82e0aa', '#abebc6', '#d5f5e3', '#eafaf1'],                  'yukon golde':    ['#7d6608', '#9a7d0a', '#b7950b', '#d4ac0d', '#f1c40f', '#f4d03f', '#f7dc6f', '#f9e79f', '#fcf3cf', '#fef9e7'],                  'raw umber':      ['#7e5109', '#9c640c', '#b9770e', '#d68910', '#f39c12', '#f5b041', '#f8c471', '#fad7a0', '#fdebd0', '#fef5e7'],                  'raw umber2':     ['#784212', '#935116', '#af601a', '#ca6f1e', '#e67e22', '#eb984e', '#f0b27a', '#f5cba7', '#fae5d3', '#fdf2e9'],                  'chocolate':      ['#6e2c00', '#873600', '#a04000', '#ba4a00', '#d35400', '#dc7633', '#e59866', '#edbb99', '#f6ddcc', '#fbeee6'],                  'oslo grey':      ['#7b7d7d', '#979a9a', '#b3b6b7', '#d0d3d4', '#ecf0f1', '#f0f3f4', '#f4f6f7', '#f7f9f9', '#fbfcfc', '#fdfefe'],                  'mid grey':       ['#626567', '#797d7f', '#909497', '#a6acaf', '#bdc3c7', '#cacfd2', '#d7dbdd', '#e5e7e9', '#f2f3f4', '#f8f9f9'],                  'mako':           ['#4d5656', '#5f6a6a', '#717d7e', '#839192', '#95a5a6', '#aab7b8', '#bfc9ca', '#d5dbdb', '#eaeded', '#f4f6f6'],                  'dark slate':     ['#424949', '#515a5a', '#616a6b', '#707b7c', '#7f8c8d', '#99a3a4', '#b2babb', '#ccd1d1', '#e5e8e8', '#f2f4f4'],                  'blue charcoal':  ['#1b2631', '#212f3c', '#283747', '#2e4053', '#34495e', '#5d6d7e', '#85929e', '#aeb6bf', '#d6dbdf', '#ebedef'],                  'black pearl':    ['#17202a', '#1c2833', '#212f3d', '#273746', '#2c3e50', '#566573', '#808b96', '#abb2b9', '#d5d8dc', '#eaecee']}    web_color = {'color a': ['#FFFF00', '#FFFF33', '#FFFF66', '#FFFF99', '#FFFFCC', '#FFFFFF', '#CCFFFF', '#CCFFCC', '#CCFF99', '#CCFF66', '#CCFF33', '#CCFF00'],                 'color b': ['#FFCC00', '#FFCC33', '#FFCC66', '#FFCC99', '#FFCCCC', '#FFCCFF', '#CCCCFF', '#CCCCCC', '#CCCC99', '#CCCC66', '#CCCC33', '#CCCC00'],                 'color c': ['#FF9900', '#FF9933', '#FF9966', '#FF9999', '#FF99CC', '#FF99FF', '#CC99FF', '#CC99CC', '#CC9999', '#CC9966', '#CC9933', '#CC9900'],                 'color d': ['#FF6600', '#FF6633', '#FF6666', '#FF6699', '#FF66CC', '#FF66FF', '#CC66FF', '#CC66CC', '#CC6699', '#CC6666', '#CC6633', '#CC6600'],                 'color e': ['#FF3300', '#FF3333', '#FF3366', '#FF3399', '#FF33CC', '#FF33FF', '#CC33FF', '#CC33CC', '#CC3399', '#CC3366', '#CC3333', '#CC3300'],                 'color f ':['#FF0000', '#FF0033', '#FF0066', '#FF0099', '#FF00CC', '#FF00FF', '#CC00FF', '#CC00CC', '#CC0099', '#CC0066', '#CC0033', '#CC0000'],                 'color g': ['#990000', '#990033', '#990066', '#990099', '#9900CC', '#9900FF', '#6600FF', '#6600CC', '#660099', '#660066', '#660033', '#660000']}    if style == 'Material Color':        if names:            return list(material_color.keys())        return material_color    if style == 'Flat Color':        if names:            return list(material_color.keys())        return flat_color    if style == 'Web Color':        return web_color    return 'Style: Material Color, Flat Color, Web Color'
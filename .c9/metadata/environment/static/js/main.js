{"filter":false,"title":"main.js","tooltip":"/static/js/main.js","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":10,"column":8},"end":{"row":15,"column":5},"action":"remove","lines":["//  var recipeData = {","        //           \"Italian\": 4, ","        //           \"Mexican\": 3, ","        //           \"Other\": 4","        //         }","     "],"id":1207}],[{"start":{"row":4,"column":9},"end":{"row":9,"column":5},"action":"insert","lines":["//  var recipeData = {","        //           \"Italian\": 4, ","        //           \"Mexican\": 3, ","        //           \"Other\": 4","        //         }","     "],"id":1208}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":54},"action":"remove","lines":["// d3.json( \"{{url_for('data') }}\", makeChart)"],"id":1209}],[{"start":{"row":9,"column":5},"end":{"row":9,"column":51},"action":"insert","lines":["// d3.json( \"{{url_for('data') }}\", makeChart)"],"id":1210}],[{"start":{"row":11,"column":4},"end":{"row":28,"column":23},"action":"remove","lines":["    var recipeData = $.get('/data')","        ","","    ","        ","   ","         var ndx = crossfilter(recipeData);","            var type_dim = ndx.dimension(dc.pluck('Type'));","            var amount =  type_dim.group().reduceSum(dc.pluck('Amount'));","            dc.pieChart('#chart-here')","                .height(330)","                .radius(90)","                .transitionDuration(1500)","                .dimension(type_dim)","                .group(amount);","","        ","        dc.renderAll();"],"id":1211}],[{"start":{"row":16,"column":4},"end":{"row":33,"column":23},"action":"insert","lines":["    var recipeData = $.get('/data')","        ","","    ","        ","   ","         var ndx = crossfilter(recipeData);","            var type_dim = ndx.dimension(dc.pluck('Type'));","            var amount =  type_dim.group().reduceSum(dc.pluck('Amount'));","            dc.pieChart('#chart-here')","                .height(330)","                .radius(90)","                .transitionDuration(1500)","                .dimension(type_dim)","                .group(amount);","","        ","        dc.renderAll();"],"id":1212}],[{"start":{"row":21,"column":2},"end":{"row":21,"column":3},"action":"remove","lines":[" "],"id":1213},{"start":{"row":21,"column":1},"end":{"row":21,"column":2},"action":"remove","lines":[" "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":1},"action":"remove","lines":[" "]},{"start":{"row":20,"column":8},"end":{"row":21,"column":0},"action":"remove","lines":["",""]},{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":20,"column":0},"action":"remove","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["",""]},{"start":{"row":17,"column":8},"end":{"row":18,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["c"],"id":1214},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["o"]},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["n"]},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["s"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["o"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["l"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["e"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["."]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["l"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["o"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["g"]}],[{"start":{"row":17,"column":19},"end":{"row":17,"column":21},"action":"insert","lines":["()"],"id":1215}],[{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["r"],"id":1216},{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["e"]},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["c"]},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["i"]},{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["p"]},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":20},"end":{"row":17,"column":26},"action":"remove","lines":["recipe"],"id":1217},{"start":{"row":17,"column":20},"end":{"row":17,"column":30},"action":"insert","lines":["recipeData"]}],[{"start":{"row":15,"column":0},"end":{"row":29,"column":23},"action":"remove","lines":["    ","        var recipeData = $.get('/data')","        console.log(recipeData)","         var ndx = crossfilter(recipeData);","            var type_dim = ndx.dimension(dc.pluck('Type'));","            var amount =  type_dim.group().reduceSum(dc.pluck('Amount'));","            dc.pieChart('#chart-here')","                .height(330)","                .radius(90)","                .transitionDuration(1500)","                .dimension(type_dim)","                .group(amount);","","        ","        dc.renderAll();"],"id":1218}],[{"start":{"row":11,"column":4},"end":{"row":25,"column":23},"action":"insert","lines":["    ","        var recipeData = $.get('/data')","        console.log(recipeData)","         var ndx = crossfilter(recipeData);","            var type_dim = ndx.dimension(dc.pluck('Type'));","            var amount =  type_dim.group().reduceSum(dc.pluck('Amount'));","            dc.pieChart('#chart-here')","                .height(330)","                .radius(90)","                .transitionDuration(1500)","                .dimension(type_dim)","                .group(amount);","","        ","        dc.renderAll();"],"id":1219}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":39},"action":"remove","lines":[" var recipeData = $.get('/data')"],"id":1220}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"remove","lines":[" "],"id":1221},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"remove","lines":[" "]},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":[" "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":8},"end":{"row":12,"column":0},"action":"remove","lines":["",""]},{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "],"id":1222},{"start":{"row":10,"column":2},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":51},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":1223},{"start":{"row":10,"column":0},"end":{"row":10,"column":5},"action":"insert","lines":["     "]},{"start":{"row":10,"column":5},"end":{"row":11,"column":0},"action":"insert","lines":["",""]},{"start":{"row":11,"column":0},"end":{"row":11,"column":5},"action":"insert","lines":["     "]}],[{"start":{"row":11,"column":5},"end":{"row":11,"column":124},"action":"insert","lines":["[{\"Type\": \"Mexican\", \"Amount\": mexican }, {\"Type\": \"Italian\", \"Amount\": italian }, {\"Type\": \"Other\", \"Amount\": other }]"],"id":1237}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":11},"action":"insert","lines":["// "],"id":1238},{"start":{"row":14,"column":8},"end":{"row":14,"column":11},"action":"insert","lines":["// "]},{"start":{"row":15,"column":8},"end":{"row":15,"column":11},"action":"insert","lines":["// "]},{"start":{"row":16,"column":8},"end":{"row":16,"column":11},"action":"insert","lines":["// "]},{"start":{"row":17,"column":8},"end":{"row":17,"column":11},"action":"insert","lines":["// "]},{"start":{"row":18,"column":8},"end":{"row":18,"column":11},"action":"insert","lines":["// "]},{"start":{"row":19,"column":8},"end":{"row":19,"column":11},"action":"insert","lines":["// "]},{"start":{"row":20,"column":8},"end":{"row":20,"column":11},"action":"insert","lines":["// "]},{"start":{"row":21,"column":8},"end":{"row":21,"column":11},"action":"insert","lines":["// "]},{"start":{"row":22,"column":8},"end":{"row":22,"column":11},"action":"insert","lines":["// "]},{"start":{"row":25,"column":8},"end":{"row":25,"column":11},"action":"insert","lines":["// "]}],[{"start":{"row":11,"column":41},"end":{"row":11,"column":42},"action":"remove","lines":["a"],"id":1239},{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"remove","lines":["c"]},{"start":{"row":11,"column":39},"end":{"row":11,"column":40},"action":"remove","lines":["i"]},{"start":{"row":11,"column":38},"end":{"row":11,"column":39},"action":"remove","lines":["x"]},{"start":{"row":11,"column":37},"end":{"row":11,"column":38},"action":"remove","lines":["e"]},{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"remove","lines":["m"]}],[{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"remove","lines":["n"],"id":1240}],[{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"insert","lines":["3"],"id":1241}],[{"start":{"row":11,"column":77},"end":{"row":11,"column":78},"action":"remove","lines":["n"],"id":1242},{"start":{"row":11,"column":76},"end":{"row":11,"column":77},"action":"remove","lines":["a"]},{"start":{"row":11,"column":75},"end":{"row":11,"column":76},"action":"remove","lines":["i"]},{"start":{"row":11,"column":74},"end":{"row":11,"column":75},"action":"remove","lines":["l"]},{"start":{"row":11,"column":73},"end":{"row":11,"column":74},"action":"remove","lines":["a"]},{"start":{"row":11,"column":72},"end":{"row":11,"column":73},"action":"remove","lines":["t"]},{"start":{"row":11,"column":71},"end":{"row":11,"column":72},"action":"remove","lines":["i"]}],[{"start":{"row":11,"column":71},"end":{"row":11,"column":72},"action":"insert","lines":["4"],"id":1243}],[{"start":{"row":11,"column":108},"end":{"row":11,"column":109},"action":"remove","lines":["r"],"id":1244},{"start":{"row":11,"column":107},"end":{"row":11,"column":108},"action":"remove","lines":["e"]},{"start":{"row":11,"column":106},"end":{"row":11,"column":107},"action":"remove","lines":["h"]},{"start":{"row":11,"column":105},"end":{"row":11,"column":106},"action":"remove","lines":["t"]},{"start":{"row":11,"column":104},"end":{"row":11,"column":105},"action":"remove","lines":["o"]}],[{"start":{"row":11,"column":104},"end":{"row":11,"column":105},"action":"insert","lines":["3"],"id":1245}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":7},"action":"insert","lines":["// "],"id":1246}],[{"start":{"row":11,"column":111},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":1247},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":15,"column":3},"action":"insert","lines":["d3.json(\"/data/employees.json\").then(function(data) {","  console.log(data[0]);","});"],"id":1248}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":[" "],"id":1249},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":[" "]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":[" "]},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":13,"column":19},"end":{"row":13,"column":33},"action":"remove","lines":["employees.json"],"id":1250},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["/"]}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"remove","lines":["/"],"id":1251}],[{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["{"],"id":1252},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["{"]}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":[" "],"id":1253},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["u"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["r"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["l"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["_"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["f"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["o"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["("],"id":1254}],[{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":[")"],"id":1255}],[{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":[" "],"id":1256},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["}"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["}"]}],[{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["'"],"id":1257}],[{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["'"],"id":1258}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":3},"action":"insert","lines":["// "],"id":1259},{"start":{"row":14,"column":0},"end":{"row":14,"column":3},"action":"insert","lines":["// "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":3},"action":"insert","lines":["// "]}],[{"start":{"row":15,"column":10},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":1260},{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":0},"end":{"row":20,"column":23},"action":"insert","lines":["queue()","    .defer(d3.json, \"/donorschoose/projects\")","    .defer(d3.json, \"static/geojson/us-states.json\")","    .await(makeGraphs);"],"id":1262}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "],"id":1263}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"insert","lines":["    "],"id":1264}],[{"start":{"row":19,"column":1},"end":{"row":19,"column":52},"action":"remove","lines":["   .defer(d3.json, \"static/geojson/us-states.json\")"],"id":1265},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"remove","lines":[" "]},{"start":{"row":18,"column":45},"end":{"row":19,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":22},"end":{"row":18,"column":43},"action":"remove","lines":["donorschoose/projects"],"id":1266},{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":["d"]},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["a"]},{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":["t"]},{"start":{"row":18,"column":25},"end":{"row":18,"column":26},"action":"insert","lines":["a"]}],[{"start":{"row":19,"column":23},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":1267},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"insert","lines":["",""]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":23,"column":2},"action":"insert","lines":["function makeGraphs(error, projectsJson, statesJson) {","    ...","};"],"id":1268}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":7},"action":"remove","lines":["..."],"id":1269}],[{"start":{"row":21,"column":44},"end":{"row":21,"column":55},"action":"remove","lines":[" statesJson"],"id":1270},{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"remove","lines":[","]}],[{"start":{"row":21,"column":43},"end":{"row":21,"column":44},"action":"insert","lines":[","],"id":1271}],[{"start":{"row":21,"column":44},"end":{"row":21,"column":45},"action":"insert","lines":[" "],"id":1272}],[{"start":{"row":21,"column":38},"end":{"row":21,"column":39},"action":"remove","lines":["s"],"id":1273},{"start":{"row":21,"column":37},"end":{"row":21,"column":38},"action":"remove","lines":["t"]},{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"remove","lines":["c"]},{"start":{"row":21,"column":35},"end":{"row":21,"column":36},"action":"remove","lines":["e"]},{"start":{"row":21,"column":34},"end":{"row":21,"column":35},"action":"remove","lines":["j"]},{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"remove","lines":["o"]},{"start":{"row":21,"column":32},"end":{"row":21,"column":33},"action":"remove","lines":["r"]},{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"remove","lines":["p"]}],[{"start":{"row":21,"column":31},"end":{"row":21,"column":32},"action":"insert","lines":["m"],"id":1274},{"start":{"row":21,"column":32},"end":{"row":21,"column":33},"action":"insert","lines":["y"]},{"start":{"row":21,"column":33},"end":{"row":21,"column":34},"action":"insert","lines":["D"]},{"start":{"row":21,"column":34},"end":{"row":21,"column":35},"action":"insert","lines":["a"]},{"start":{"row":21,"column":35},"end":{"row":21,"column":36},"action":"insert","lines":["t"]},{"start":{"row":21,"column":36},"end":{"row":21,"column":37},"action":"insert","lines":["a"]}],[{"start":{"row":21,"column":42},"end":{"row":21,"column":43},"action":"remove","lines":[" "],"id":1275},{"start":{"row":21,"column":41},"end":{"row":21,"column":42},"action":"remove","lines":[","]}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":11},"action":"remove","lines":["// "],"id":1276},{"start":{"row":26,"column":8},"end":{"row":26,"column":11},"action":"remove","lines":["// "]},{"start":{"row":27,"column":8},"end":{"row":27,"column":11},"action":"remove","lines":["// "]},{"start":{"row":28,"column":8},"end":{"row":28,"column":11},"action":"remove","lines":["// "]},{"start":{"row":29,"column":8},"end":{"row":29,"column":11},"action":"remove","lines":["// "]},{"start":{"row":30,"column":8},"end":{"row":30,"column":11},"action":"remove","lines":["// "]},{"start":{"row":31,"column":8},"end":{"row":31,"column":11},"action":"remove","lines":["// "]},{"start":{"row":32,"column":8},"end":{"row":32,"column":11},"action":"remove","lines":["// "]},{"start":{"row":33,"column":8},"end":{"row":33,"column":11},"action":"remove","lines":["// "]},{"start":{"row":34,"column":8},"end":{"row":34,"column":11},"action":"remove","lines":["// "]},{"start":{"row":37,"column":8},"end":{"row":37,"column":11},"action":"remove","lines":["// "]}],[{"start":{"row":25,"column":5},"end":{"row":25,"column":31},"action":"remove","lines":["   console.log(recipeData)"],"id":1277}],[{"start":{"row":26,"column":9},"end":{"row":37,"column":23},"action":"remove","lines":["var ndx = crossfilter(recipeData);","            var type_dim = ndx.dimension(dc.pluck('Type'));","            var amount =  type_dim.group().reduceSum(dc.pluck('Amount'));","            dc.pieChart('#chart-here')","                .height(330)","                .radius(90)","                .transitionDuration(1500)","                .dimension(type_dim)","                .group(amount);","","        ","        dc.renderAll();"],"id":1278}],[{"start":{"row":21,"column":44},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":1279},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":22,"column":8},"end":{"row":33,"column":23},"action":"insert","lines":["var ndx = crossfilter(recipeData);","            var type_dim = ndx.dimension(dc.pluck('Type'));","            var amount =  type_dim.group().reduceSum(dc.pluck('Amount'));","            dc.pieChart('#chart-here')","                .height(330)","                .radius(90)","                .transitionDuration(1500)","                .dimension(type_dim)","                .group(amount);","","        ","        dc.renderAll();"],"id":1280}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":1},"action":"remove","lines":[" "],"id":1281},{"start":{"row":33,"column":23},"end":{"row":34,"column":3},"action":"remove","lines":["","   "]}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":1},"action":"remove","lines":[" "],"id":1282},{"start":{"row":31,"column":0},"end":{"row":32,"column":7},"action":"remove","lines":["","       "]}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":40},"action":"remove","lines":["recipeData"],"id":1283}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":40},"action":"insert","lines":["myDataJson"],"id":1284}],[{"start":{"row":12,"column":2},"end":{"row":16,"column":0},"action":"remove","lines":["  ","//     d3.json(\"{{ url_for('data') }}\").then(function(data) {","//   console.log(data[0]);","//     });",""],"id":1285}],[{"start":{"row":9,"column":2},"end":{"row":9,"column":51},"action":"remove","lines":["   // d3.json( \"{{url_for('data') }}\", makeChart)"],"id":1286},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"remove","lines":[" "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":10,"column":5},"end":{"row":11,"column":111},"action":"remove","lines":["","    //  [{\"Type\": \"Mexican\", \"Amount\": 3 }, {\"Type\": \"Italian\", \"Amount\": 4 }, {\"Type\": \"Other\", \"Amount\": 3 }]"],"id":1287},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":[" "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["",""]},{"start":{"row":8,"column":20},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "],"id":1288}],[{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["s"],"id":1289}],[{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"remove","lines":["s"],"id":1290}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":[" "],"id":1291}],[{"start":{"row":0,"column":0},"end":{"row":9,"column":2},"action":"remove","lines":["// $('.card').hover(","    //   function(){ $(this).addClass('inverse') },","    //   function(){ $(this).removeClass('inverse') }","    // );","         //  var recipeData = {","        //           \"Italian\": 4, ","        //           \"Mexican\": 3, ","        //           \"Other\": 4","        //         }","  "],"id":1292}],[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */","var prevScrollpos = window.pageYOffset;","window.onscroll = function() {","  var currentScrollPos = window.pageYOffset;","  if (prevScrollpos > currentScrollPos) {","    document.getElementById(\"navbar\").style.top = \"0\";","  } else {","    document.getElementById(\"navbar\").style.top = \"-50px\";","  }","  prevScrollpos = currentScrollPos;","}"],"id":1293}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":27},"action":"remove","lines":["getElementById"],"id":1294},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["q"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["u"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["e"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["r"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["y"]}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":18},"action":"remove","lines":["query"],"id":1295},{"start":{"row":5,"column":13},"end":{"row":5,"column":26},"action":"insert","lines":["querySelector"]}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["."],"id":1296}],[{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"insert","lines":["-"],"id":1297},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"insert","lines":["w"]},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"insert","lines":["r"]},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"insert","lines":["a"]},{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"insert","lines":["p"]},{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"insert","lines":["p"]},{"start":{"row":5,"column":41},"end":{"row":5,"column":42},"action":"insert","lines":["e"]},{"start":{"row":5,"column":42},"end":{"row":5,"column":43},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":13},"end":{"row":7,"column":37},"action":"remove","lines":["getElementById(\"navbar\")"],"id":1298}],[{"start":{"row":7,"column":13},"end":{"row":7,"column":45},"action":"insert","lines":["querySelector(\".navbar-wrapper\")"],"id":1299}],[{"start":{"row":7,"column":60},"end":{"row":7,"column":61},"action":"remove","lines":["5"],"id":1300}],[{"start":{"row":7,"column":60},"end":{"row":7,"column":61},"action":"insert","lines":["7"],"id":1301}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":1302},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["C"],"id":1303},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["e"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["d"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["i"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[":"]}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":[" "],"id":1304}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":71},"action":"insert","lines":["https://www.w3schools.com/howto/howto_js_navbar_hide_scroll.asp"],"id":1305}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":3},"action":"insert","lines":["// "],"id":1306}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":74},"action":"remove","lines":["// Credit: https://www.w3schools.com/howto/howto_js_navbar_hide_scroll.asp"],"id":1307}],[{"start":{"row":12,"column":1},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":1308},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":74},"action":"insert","lines":["// Credit: https://www.w3schools.com/howto/howto_js_navbar_hide_scroll.asp"],"id":1309}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":[";"],"id":1310}],[{"start":{"row":39,"column":2},"end":{"row":41,"column":3},"action":"insert","lines":["$(\".fadeMe\").hide().each(function(i) {","  $(this).delay(i*1500).fadeIn(1500);","});"],"id":1311}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":3},"action":"insert","lines":["// "],"id":1312},{"start":{"row":40,"column":0},"end":{"row":40,"column":3},"action":"insert","lines":["// "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":3},"action":"insert","lines":["// "]}],[{"start":{"row":41,"column":6},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":1313},{"start":{"row":42,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":43,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["// intro fadeIn (tcloniger code)","    ","    /* Every time the window is scrolled ... */","    $(window).scroll( function(){","    ","        /* Check the location of each desired element */","        $('.hidden').each( function(i){","            ","            var bottom_of_object = $(this).position().top + $(this).outerHeight();","            var bottom_of_window = $(window).scrollTop() + $(window).height();","            ","            /* If the object is completely visible in the window, fade it it */","            if( bottom_of_window > bottom_of_object ){","                ","                $(this).animate({'opacity':'1'},3000);","                    ","            }","            ","        }); ","    ","    });","    "],"id":1314}],[{"start":{"row":49,"column":17},"end":{"row":49,"column":18},"action":"remove","lines":["n"],"id":1315},{"start":{"row":49,"column":16},"end":{"row":49,"column":17},"action":"remove","lines":["e"]},{"start":{"row":49,"column":15},"end":{"row":49,"column":16},"action":"remove","lines":["d"]},{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"remove","lines":["d"]},{"start":{"row":49,"column":13},"end":{"row":49,"column":14},"action":"remove","lines":["i"]},{"start":{"row":49,"column":12},"end":{"row":49,"column":13},"action":"remove","lines":["h"]}],[{"start":{"row":49,"column":12},"end":{"row":49,"column":13},"action":"insert","lines":["f"],"id":1316},{"start":{"row":49,"column":13},"end":{"row":49,"column":14},"action":"insert","lines":["a"]},{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"insert","lines":["d"]},{"start":{"row":49,"column":15},"end":{"row":49,"column":16},"action":"insert","lines":["e"]},{"start":{"row":49,"column":16},"end":{"row":49,"column":17},"action":"insert","lines":["M"]},{"start":{"row":49,"column":17},"end":{"row":49,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":3},"action":"remove","lines":["// "],"id":1317},{"start":{"row":40,"column":0},"end":{"row":40,"column":3},"action":"remove","lines":["// "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":3},"action":"remove","lines":["// "]}],[{"start":{"row":39,"column":16},"end":{"row":39,"column":21},"action":"remove","lines":["ide()"],"id":1318},{"start":{"row":39,"column":15},"end":{"row":39,"column":16},"action":"remove","lines":["h"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"remove","lines":["."]}],[{"start":{"row":40,"column":2},"end":{"row":40,"column":37},"action":"remove","lines":["$(this).delay(i*1500).fadeIn(1500);"],"id":1319},{"start":{"row":40,"column":2},"end":{"row":40,"column":40},"action":"insert","lines":["$(this).animate({'opacity':'1'},3000);"]}],[{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["1"],"id":1320}],[{"start":{"row":49,"column":18},"end":{"row":49,"column":19},"action":"insert","lines":["2"],"id":1321}]]},"ace":{"folds":[],"scrolltop":581,"scrollleft":0,"selection":{"start":{"row":49,"column":19},"end":{"row":49,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":35,"state":"start","mode":"ace/mode/javascript"}},"timestamp":1568401655019,"hash":"801c1e008ff56768098a3ecb503926be9a54ef56"}
{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":[" "],"id":831}],[{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"insert","lines":["4"],"id":832}],[{"start":{"row":40,"column":57},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":833},{"start":{"row":41,"column":0},"end":{"row":41,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":40,"column":57},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":834},{"start":{"row":41,"column":0},"end":{"row":41,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":41,"column":3},"end":{"row":42,"column":54},"action":"insert","lines":["recipes = coll_recipes.find().sort('_id', pymongo.ASCENDING).skip(","    #     (current_page - 1)*per_page).limit(per_page)"],"id":835}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":6},"action":"remove","lines":["# "],"id":836}],[{"start":{"row":41,"column":13},"end":{"row":41,"column":25},"action":"remove","lines":["coll_recipes"],"id":837}],[{"start":{"row":41,"column":13},"end":{"row":41,"column":14},"action":"insert","lines":["m"],"id":838},{"start":{"row":41,"column":14},"end":{"row":41,"column":15},"action":"insert","lines":["o"]},{"start":{"row":41,"column":15},"end":{"row":41,"column":16},"action":"insert","lines":["n"]},{"start":{"row":41,"column":16},"end":{"row":41,"column":17},"action":"insert","lines":["g"]},{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":["o"]},{"start":{"row":41,"column":18},"end":{"row":41,"column":19},"action":"insert","lines":["."]}],[{"start":{"row":41,"column":19},"end":{"row":41,"column":20},"action":"insert","lines":["d"],"id":839},{"start":{"row":41,"column":20},"end":{"row":41,"column":21},"action":"insert","lines":["b"]},{"start":{"row":41,"column":21},"end":{"row":41,"column":22},"action":"insert","lines":["."]},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["r"]},{"start":{"row":41,"column":23},"end":{"row":41,"column":24},"action":"insert","lines":["e"]},{"start":{"row":41,"column":24},"end":{"row":41,"column":25},"action":"insert","lines":["c"]},{"start":{"row":41,"column":25},"end":{"row":41,"column":26},"action":"insert","lines":["i"]},{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"remove","lines":["e"],"id":840}],[{"start":{"row":41,"column":26},"end":{"row":41,"column":27},"action":"insert","lines":["p"],"id":841},{"start":{"row":41,"column":27},"end":{"row":41,"column":28},"action":"insert","lines":["e"]},{"start":{"row":41,"column":28},"end":{"row":41,"column":29},"action":"insert","lines":["s"]}],[{"start":{"row":42,"column":27},"end":{"row":42,"column":28},"action":"insert","lines":[" "],"id":842},{"start":{"row":42,"column":28},"end":{"row":42,"column":29},"action":"insert","lines":["r"]},{"start":{"row":42,"column":29},"end":{"row":42,"column":30},"action":"insert","lines":["e"]},{"start":{"row":42,"column":30},"end":{"row":42,"column":31},"action":"insert","lines":["c"]},{"start":{"row":42,"column":31},"end":{"row":42,"column":32},"action":"insert","lines":["i"]},{"start":{"row":42,"column":32},"end":{"row":42,"column":33},"action":"insert","lines":["p"]},{"start":{"row":42,"column":33},"end":{"row":42,"column":34},"action":"insert","lines":["e"]},{"start":{"row":42,"column":34},"end":{"row":42,"column":35},"action":"insert","lines":["s"]}],[{"start":{"row":42,"column":35},"end":{"row":42,"column":36},"action":"insert","lines":["_"],"id":843}],[{"start":{"row":42,"column":52},"end":{"row":42,"column":53},"action":"insert","lines":["r"],"id":844},{"start":{"row":42,"column":53},"end":{"row":42,"column":54},"action":"insert","lines":["e"]},{"start":{"row":42,"column":54},"end":{"row":42,"column":55},"action":"insert","lines":["c"]},{"start":{"row":42,"column":55},"end":{"row":42,"column":56},"action":"insert","lines":["i"]},{"start":{"row":42,"column":56},"end":{"row":42,"column":57},"action":"insert","lines":["p"]},{"start":{"row":42,"column":57},"end":{"row":42,"column":58},"action":"insert","lines":["e"]},{"start":{"row":42,"column":58},"end":{"row":42,"column":59},"action":"insert","lines":["s"]},{"start":{"row":42,"column":59},"end":{"row":42,"column":60},"action":"insert","lines":["_"]}],[{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"remove","lines":["_"],"id":845},{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"remove","lines":["t"]},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"remove","lines":["n"]},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"remove","lines":["e"]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"remove","lines":["r"]},{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"remove","lines":["r"]},{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"remove","lines":["u"]},{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"remove","lines":["c"]}],[{"start":{"row":37,"column":3},"end":{"row":42,"column":61},"action":"remove","lines":["recipes_per_page = 4","   page = int(request.args.get('page', 1))","   all_recipes = mongo.db.recipes.count()","   pages = range(1, int(math.ceil(total / per_page)) + 1)","   recipes = mongo.db.recipes.find().sort('_id', pymongo.ASCENDING).skip(","        (page - 1)* recipes_per_page).limit(recipes_per_page)"],"id":846}],[{"start":{"row":33,"column":83},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":847},{"start":{"row":34,"column":0},"end":{"row":34,"column":12},"action":"insert","lines":["            "]},{"start":{"row":34,"column":12},"end":{"row":35,"column":0},"action":"insert","lines":["",""]},{"start":{"row":35,"column":0},"end":{"row":35,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":35,"column":8},"end":{"row":35,"column":12},"action":"remove","lines":["    "],"id":848},{"start":{"row":35,"column":4},"end":{"row":35,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":35,"column":4},"end":{"row":40,"column":61},"action":"insert","lines":["recipes_per_page = 4","   page = int(request.args.get('page', 1))","   all_recipes = mongo.db.recipes.count()","   pages = range(1, int(math.ceil(total / per_page)) + 1)","   recipes = mongo.db.recipes.find().sort('_id', pymongo.ASCENDING).skip(","        (page - 1)* recipes_per_page).limit(recipes_per_page)"],"id":849}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"remove","lines":["    "],"id":850}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":1},"action":"insert","lines":[" "],"id":851},{"start":{"row":35,"column":1},"end":{"row":35,"column":2},"action":"insert","lines":[" "]},{"start":{"row":35,"column":2},"end":{"row":35,"column":3},"action":"insert","lines":[" "]}],[{"start":{"row":42,"column":51},"end":{"row":42,"column":74},"action":"remove","lines":["mongo.db.recipes.find()"],"id":852},{"start":{"row":42,"column":51},"end":{"row":42,"column":52},"action":"insert","lines":["r"]},{"start":{"row":42,"column":52},"end":{"row":42,"column":53},"action":"insert","lines":["e"]},{"start":{"row":42,"column":53},"end":{"row":42,"column":54},"action":"insert","lines":["c"]},{"start":{"row":42,"column":54},"end":{"row":42,"column":55},"action":"insert","lines":["i"]},{"start":{"row":42,"column":55},"end":{"row":42,"column":56},"action":"insert","lines":["p"]},{"start":{"row":42,"column":56},"end":{"row":42,"column":57},"action":"insert","lines":["e"]},{"start":{"row":42,"column":57},"end":{"row":42,"column":58},"action":"insert","lines":["s"]}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "],"id":853},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":6},"end":{"row":35,"column":7},"action":"remove","lines":[" "],"id":855},{"start":{"row":35,"column":5},"end":{"row":35,"column":6},"action":"remove","lines":[" "]},{"start":{"row":35,"column":4},"end":{"row":35,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"remove","lines":[" "],"id":856},{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"remove","lines":[" "]},{"start":{"row":36,"column":4},"end":{"row":36,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"remove","lines":[" "],"id":857},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"remove","lines":[" "]},{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":38,"column":6},"end":{"row":38,"column":7},"action":"remove","lines":[" "],"id":858},{"start":{"row":38,"column":5},"end":{"row":38,"column":6},"action":"remove","lines":[" "]},{"start":{"row":38,"column":4},"end":{"row":38,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"remove","lines":[" "],"id":859},{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"remove","lines":[" "]},{"start":{"row":39,"column":4},"end":{"row":39,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":40,"column":8},"end":{"row":40,"column":12},"action":"remove","lines":["    "],"id":860},{"start":{"row":40,"column":4},"end":{"row":40,"column":8},"action":"remove","lines":["    "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":1},"action":"insert","lines":[" "],"id":861},{"start":{"row":40,"column":1},"end":{"row":40,"column":2},"action":"insert","lines":[" "]},{"start":{"row":40,"column":2},"end":{"row":40,"column":3},"action":"insert","lines":[" "]},{"start":{"row":40,"column":3},"end":{"row":40,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":6},"action":"insert","lines":["# "],"id":862},{"start":{"row":36,"column":4},"end":{"row":36,"column":6},"action":"insert","lines":["# "]},{"start":{"row":37,"column":4},"end":{"row":37,"column":6},"action":"insert","lines":["# "]},{"start":{"row":38,"column":4},"end":{"row":38,"column":6},"action":"insert","lines":["# "]},{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"insert","lines":["# "]},{"start":{"row":40,"column":4},"end":{"row":40,"column":6},"action":"insert","lines":["# "]},{"start":{"row":42,"column":4},"end":{"row":42,"column":6},"action":"insert","lines":["# "]}],[{"start":{"row":43,"column":4},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":863},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":44,"column":4},"end":{"row":44,"column":5},"action":"insert","lines":["m"]}],[{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["o"],"id":864},{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":["n"]},{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["g"]},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["."]},{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["d"]}],[{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"remove","lines":["d"],"id":865},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"remove","lines":["."]}],[{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["o"],"id":866},{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["."]},{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["d"]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["b"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["."]},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["r"]},{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":["e"]},{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":["c"]},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["i"]},{"start":{"row":44,"column":17},"end":{"row":44,"column":18},"action":"insert","lines":["p"]},{"start":{"row":44,"column":18},"end":{"row":44,"column":19},"action":"insert","lines":["e"]},{"start":{"row":44,"column":19},"end":{"row":44,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":["."],"id":867},{"start":{"row":44,"column":21},"end":{"row":44,"column":22},"action":"insert","lines":["f"]},{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"insert","lines":["i"]},{"start":{"row":44,"column":23},"end":{"row":44,"column":24},"action":"insert","lines":["n"]},{"start":{"row":44,"column":24},"end":{"row":44,"column":25},"action":"insert","lines":["d"]}],[{"start":{"row":44,"column":25},"end":{"row":44,"column":27},"action":"insert","lines":["()"],"id":868}],[{"start":{"row":44,"column":27},"end":{"row":44,"column":28},"action":"insert","lines":["."],"id":869},{"start":{"row":44,"column":28},"end":{"row":44,"column":29},"action":"insert","lines":["s"]},{"start":{"row":44,"column":29},"end":{"row":44,"column":30},"action":"insert","lines":["k"]},{"start":{"row":44,"column":30},"end":{"row":44,"column":31},"action":"insert","lines":["i"]},{"start":{"row":44,"column":31},"end":{"row":44,"column":32},"action":"insert","lines":["p"]}],[{"start":{"row":44,"column":32},"end":{"row":44,"column":34},"action":"insert","lines":["()"],"id":870}],[{"start":{"row":44,"column":33},"end":{"row":44,"column":35},"action":"insert","lines":["()"],"id":871}],[{"start":{"row":44,"column":34},"end":{"row":44,"column":35},"action":"insert","lines":["p"],"id":872},{"start":{"row":44,"column":35},"end":{"row":44,"column":36},"action":"insert","lines":["a"]},{"start":{"row":44,"column":36},"end":{"row":44,"column":37},"action":"insert","lines":["g"]},{"start":{"row":44,"column":37},"end":{"row":44,"column":38},"action":"insert","lines":["e"]}],[{"start":{"row":44,"column":38},"end":{"row":44,"column":39},"action":"insert","lines":[" "],"id":873},{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"insert","lines":["-"]}],[{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"insert","lines":[" "],"id":874},{"start":{"row":44,"column":41},"end":{"row":44,"column":42},"action":"insert","lines":["1"]}],[{"start":{"row":44,"column":43},"end":{"row":44,"column":44},"action":"insert","lines":[" "],"id":875},{"start":{"row":44,"column":44},"end":{"row":44,"column":45},"action":"insert","lines":["*"]}],[{"start":{"row":44,"column":45},"end":{"row":44,"column":46},"action":"insert","lines":[" "],"id":876},{"start":{"row":44,"column":46},"end":{"row":44,"column":47},"action":"insert","lines":["n"]},{"start":{"row":44,"column":47},"end":{"row":44,"column":48},"action":"insert","lines":["u"]},{"start":{"row":44,"column":48},"end":{"row":44,"column":49},"action":"insert","lines":["m"]}],[{"start":{"row":44,"column":50},"end":{"row":44,"column":51},"action":"insert","lines":["."],"id":877}],[{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"insert","lines":[" "],"id":878}],[{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"remove","lines":[" "],"id":879}],[{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"insert","lines":["l"],"id":880},{"start":{"row":44,"column":52},"end":{"row":44,"column":53},"action":"insert","lines":["i"]},{"start":{"row":44,"column":53},"end":{"row":44,"column":54},"action":"insert","lines":["m"]},{"start":{"row":44,"column":54},"end":{"row":44,"column":55},"action":"insert","lines":["i"]},{"start":{"row":44,"column":55},"end":{"row":44,"column":56},"action":"insert","lines":["t"]}],[{"start":{"row":44,"column":56},"end":{"row":44,"column":58},"action":"insert","lines":["()"],"id":881}],[{"start":{"row":44,"column":57},"end":{"row":44,"column":58},"action":"insert","lines":["n"],"id":882},{"start":{"row":44,"column":58},"end":{"row":44,"column":59},"action":"insert","lines":["u"]},{"start":{"row":44,"column":59},"end":{"row":44,"column":60},"action":"insert","lines":["m"]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":5},"action":"insert","lines":["r"],"id":883},{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["e"]},{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":["c"]},{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["i"]},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["p"]},{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":["e"]},{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":[" "],"id":884},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":[" "],"id":885}],[{"start":{"row":43,"column":4},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":886},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":24},"action":"insert","lines":["recipes_per_page = 4"],"id":887}],[{"start":{"row":45,"column":58},"end":{"row":45,"column":59},"action":"remove","lines":["m"],"id":888},{"start":{"row":45,"column":57},"end":{"row":45,"column":58},"action":"remove","lines":["u"]},{"start":{"row":45,"column":56},"end":{"row":45,"column":57},"action":"remove","lines":["n"]}],[{"start":{"row":45,"column":56},"end":{"row":45,"column":57},"action":"insert","lines":["r"],"id":889},{"start":{"row":45,"column":57},"end":{"row":45,"column":58},"action":"insert","lines":["e"]},{"start":{"row":45,"column":58},"end":{"row":45,"column":59},"action":"insert","lines":["c"]},{"start":{"row":45,"column":59},"end":{"row":45,"column":60},"action":"insert","lines":["i"]},{"start":{"row":45,"column":60},"end":{"row":45,"column":61},"action":"insert","lines":["p"]},{"start":{"row":45,"column":61},"end":{"row":45,"column":62},"action":"insert","lines":["e"]}],[{"start":{"row":45,"column":62},"end":{"row":45,"column":63},"action":"insert","lines":["_"],"id":890},{"start":{"row":45,"column":63},"end":{"row":45,"column":64},"action":"insert","lines":["p"]},{"start":{"row":45,"column":64},"end":{"row":45,"column":65},"action":"insert","lines":["e"]},{"start":{"row":45,"column":65},"end":{"row":45,"column":66},"action":"insert","lines":["r"]},{"start":{"row":45,"column":66},"end":{"row":45,"column":67},"action":"insert","lines":["_"]}],[{"start":{"row":45,"column":67},"end":{"row":45,"column":68},"action":"insert","lines":["p"],"id":891},{"start":{"row":45,"column":68},"end":{"row":45,"column":69},"action":"insert","lines":["a"]},{"start":{"row":45,"column":69},"end":{"row":45,"column":70},"action":"insert","lines":["g"]},{"start":{"row":45,"column":70},"end":{"row":45,"column":71},"action":"insert","lines":["e"]}],[{"start":{"row":45,"column":81},"end":{"row":45,"column":82},"action":"remove","lines":["m"],"id":892},{"start":{"row":45,"column":80},"end":{"row":45,"column":81},"action":"remove","lines":["u"]},{"start":{"row":45,"column":79},"end":{"row":45,"column":80},"action":"remove","lines":["n"]}],[{"start":{"row":45,"column":79},"end":{"row":45,"column":80},"action":"insert","lines":["r"],"id":893},{"start":{"row":45,"column":80},"end":{"row":45,"column":81},"action":"insert","lines":["e"]},{"start":{"row":45,"column":81},"end":{"row":45,"column":82},"action":"insert","lines":["c"]},{"start":{"row":45,"column":82},"end":{"row":45,"column":83},"action":"insert","lines":["i"]},{"start":{"row":45,"column":83},"end":{"row":45,"column":84},"action":"insert","lines":["p"]},{"start":{"row":45,"column":84},"end":{"row":45,"column":85},"action":"insert","lines":["e"]},{"start":{"row":45,"column":85},"end":{"row":45,"column":86},"action":"insert","lines":["_"]},{"start":{"row":45,"column":86},"end":{"row":45,"column":87},"action":"insert","lines":["p"]},{"start":{"row":45,"column":87},"end":{"row":45,"column":88},"action":"insert","lines":["e"]},{"start":{"row":45,"column":88},"end":{"row":45,"column":89},"action":"insert","lines":["r"]}],[{"start":{"row":45,"column":89},"end":{"row":45,"column":90},"action":"insert","lines":["_"],"id":894},{"start":{"row":45,"column":90},"end":{"row":45,"column":91},"action":"insert","lines":["p"]},{"start":{"row":45,"column":91},"end":{"row":45,"column":92},"action":"insert","lines":["a"]},{"start":{"row":45,"column":92},"end":{"row":45,"column":93},"action":"insert","lines":["g"]},{"start":{"row":45,"column":93},"end":{"row":45,"column":94},"action":"insert","lines":["e"]}],[{"start":{"row":43,"column":4},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":895},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":43},"action":"insert","lines":["page = int(request.args.get('page', 1))"],"id":896}],[{"start":{"row":44,"column":43},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":897},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":4},"end":{"row":45,"column":5},"action":"insert","lines":["a"]},{"start":{"row":45,"column":5},"end":{"row":45,"column":6},"action":"insert","lines":["l"]},{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"insert","lines":["l"]}],[{"start":{"row":45,"column":7},"end":{"row":45,"column":8},"action":"insert","lines":["_"],"id":898},{"start":{"row":45,"column":8},"end":{"row":45,"column":9},"action":"insert","lines":["r"]},{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"insert","lines":["e"]},{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"insert","lines":["c"]},{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"insert","lines":["i"]},{"start":{"row":45,"column":12},"end":{"row":45,"column":13},"action":"insert","lines":["p"]},{"start":{"row":45,"column":13},"end":{"row":45,"column":14},"action":"insert","lines":["e"]},{"start":{"row":45,"column":14},"end":{"row":45,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"insert","lines":[" "],"id":899},{"start":{"row":45,"column":16},"end":{"row":45,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":45,"column":17},"end":{"row":45,"column":18},"action":"insert","lines":[" "],"id":900}],[{"start":{"row":45,"column":18},"end":{"row":45,"column":44},"action":"insert","lines":["= mongo.db.recipes.count()"],"id":901}],[{"start":{"row":45,"column":44},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":902},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":58},"action":"insert","lines":["pages = range(1, int(math.ceil(total / per_page)) + 1)"],"id":903}],[{"start":{"row":46,"column":39},"end":{"row":46,"column":40},"action":"remove","lines":["l"],"id":904},{"start":{"row":46,"column":38},"end":{"row":46,"column":39},"action":"remove","lines":["a"]},{"start":{"row":46,"column":37},"end":{"row":46,"column":38},"action":"remove","lines":["t"]},{"start":{"row":46,"column":36},"end":{"row":46,"column":37},"action":"remove","lines":["o"]},{"start":{"row":46,"column":35},"end":{"row":46,"column":36},"action":"remove","lines":["t"]}],[{"start":{"row":46,"column":35},"end":{"row":46,"column":36},"action":"insert","lines":["a"],"id":905},{"start":{"row":46,"column":36},"end":{"row":46,"column":37},"action":"insert","lines":["l"]},{"start":{"row":46,"column":37},"end":{"row":46,"column":38},"action":"insert","lines":["l"]},{"start":{"row":46,"column":38},"end":{"row":46,"column":39},"action":"insert","lines":["_"]},{"start":{"row":46,"column":39},"end":{"row":46,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":46,"column":39},"end":{"row":46,"column":40},"action":"remove","lines":["e"],"id":906}],[{"start":{"row":46,"column":39},"end":{"row":46,"column":40},"action":"insert","lines":["r"],"id":907},{"start":{"row":46,"column":40},"end":{"row":46,"column":41},"action":"insert","lines":["e"]},{"start":{"row":46,"column":41},"end":{"row":46,"column":42},"action":"insert","lines":["c"]},{"start":{"row":46,"column":42},"end":{"row":46,"column":43},"action":"insert","lines":["i"]},{"start":{"row":46,"column":43},"end":{"row":46,"column":44},"action":"insert","lines":["p"]},{"start":{"row":46,"column":44},"end":{"row":46,"column":45},"action":"insert","lines":["e"]},{"start":{"row":46,"column":45},"end":{"row":46,"column":46},"action":"insert","lines":["s"]}],[{"start":{"row":48,"column":95},"end":{"row":49,"column":0},"action":"insert","lines":["",""],"id":908},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":49,"column":4},"end":{"row":49,"column":59},"action":"insert","lines":["return render_template(\"recipes.html\", recipes=recipes)"],"id":909}],[{"start":{"row":49,"column":58},"end":{"row":49,"column":59},"action":"insert","lines":[","],"id":910}],[{"start":{"row":49,"column":59},"end":{"row":49,"column":60},"action":"insert","lines":[" "],"id":911}],[{"start":{"row":49,"column":60},"end":{"row":49,"column":61},"action":"insert","lines":["p"],"id":912},{"start":{"row":49,"column":61},"end":{"row":49,"column":62},"action":"insert","lines":["a"]},{"start":{"row":49,"column":62},"end":{"row":49,"column":63},"action":"insert","lines":["g"]},{"start":{"row":49,"column":63},"end":{"row":49,"column":64},"action":"insert","lines":["e"]},{"start":{"row":49,"column":64},"end":{"row":49,"column":65},"action":"insert","lines":["s"]},{"start":{"row":49,"column":65},"end":{"row":49,"column":66},"action":"insert","lines":["="]},{"start":{"row":49,"column":66},"end":{"row":49,"column":67},"action":"insert","lines":["p"]},{"start":{"row":49,"column":67},"end":{"row":49,"column":68},"action":"insert","lines":["a"]},{"start":{"row":49,"column":68},"end":{"row":49,"column":69},"action":"insert","lines":["g"]},{"start":{"row":49,"column":69},"end":{"row":49,"column":70},"action":"insert","lines":["e"]},{"start":{"row":49,"column":70},"end":{"row":49,"column":71},"action":"insert","lines":["s"]}],[{"start":{"row":49,"column":71},"end":{"row":49,"column":72},"action":"insert","lines":[","],"id":913}],[{"start":{"row":49,"column":72},"end":{"row":49,"column":73},"action":"insert","lines":[" "],"id":914},{"start":{"row":49,"column":73},"end":{"row":49,"column":74},"action":"insert","lines":["p"]},{"start":{"row":49,"column":74},"end":{"row":49,"column":75},"action":"insert","lines":["a"]},{"start":{"row":49,"column":75},"end":{"row":49,"column":76},"action":"insert","lines":["g"]},{"start":{"row":49,"column":76},"end":{"row":49,"column":77},"action":"insert","lines":["e"]},{"start":{"row":49,"column":77},"end":{"row":49,"column":78},"action":"insert","lines":["="]},{"start":{"row":49,"column":78},"end":{"row":49,"column":79},"action":"insert","lines":["p"]},{"start":{"row":49,"column":79},"end":{"row":49,"column":80},"action":"insert","lines":["a"]}],[{"start":{"row":49,"column":80},"end":{"row":49,"column":81},"action":"insert","lines":["g"],"id":915},{"start":{"row":49,"column":81},"end":{"row":49,"column":82},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":0},"end":{"row":42,"column":61},"action":"remove","lines":["            ","    # return render_template(\"recipes.html\", recipes=recipes)"],"id":916}],[{"start":{"row":39,"column":52},"end":{"row":39,"column":69},"action":"remove","lines":["pymongo.ASCENDING"],"id":917}],[{"start":{"row":39,"column":52},"end":{"row":39,"column":53},"action":"insert","lines":["-"],"id":918},{"start":{"row":39,"column":53},"end":{"row":39,"column":54},"action":"insert","lines":["1"]}],[{"start":{"row":35,"column":2},"end":{"row":38,"column":60},"action":"remove","lines":["  # recipes_per_page = 4","    # page = int(request.args.get('page', 1))","    # all_recipes = mongo.db.recipes.count()","    # pages = range(1, int(math.ceil(total / per_page)) + 1)"],"id":919}],[{"start":{"row":47,"column":3},"end":{"row":63,"column":113},"action":"remove","lines":["","    ","       # Pagination","    # current_page = int(request.args.get('current_page', 1))","    # total_drinks = mongo.db.drinks.count()","    # num_pages = range(1, int(math.ceil(total_drinks / drinks_per_page)) + 1)","    # drinks = mongo.db.drinks.find().sort(sort_by, sort_order).skip(","    #     (current_page - 1) * drinks_per_page).limit(drinks_per_page)","        ","    #         per_page = 4","    # current_page = int(request.args.get('current_page', 1))","    # total = coll_recipes.count()","    # pages = range(1, int(math.ceil(total / per_page)) + 1)","    # recipes = coll_recipes.find().sort('_id', pymongo.ASCENDING).skip(","    #     (current_page - 1)*per_page).limit(per_page)","","    # return render_template('home.html', recipes=recipes, title=\"Whisk\", current_page=current_page, pages=pages)"],"id":920},{"start":{"row":47,"column":2},"end":{"row":47,"column":3},"action":"remove","lines":[" "]},{"start":{"row":47,"column":1},"end":{"row":47,"column":2},"action":"remove","lines":[" "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":1},"action":"remove","lines":[" "]},{"start":{"row":46,"column":3},"end":{"row":47,"column":0},"action":"remove","lines":["",""]},{"start":{"row":46,"column":2},"end":{"row":46,"column":3},"action":"remove","lines":[" "]},{"start":{"row":46,"column":1},"end":{"row":46,"column":2},"action":"remove","lines":[" "]}],[{"start":{"row":46,"column":0},"end":{"row":46,"column":1},"action":"remove","lines":[" "],"id":921},{"start":{"row":45,"column":83},"end":{"row":46,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":41,"column":18},"end":{"row":41,"column":19},"action":"remove","lines":["="],"id":922},{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"remove","lines":[" "]}],[{"start":{"row":0,"column":9},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":923},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["i"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["m"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["p"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["o"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":[" "],"id":924},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["m"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["a"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["t"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["h"]}],[{"start":{"row":43,"column":49},"end":{"row":43,"column":50},"action":"insert","lines":["r"],"id":925},{"start":{"row":43,"column":50},"end":{"row":43,"column":51},"action":"insert","lines":["e"]},{"start":{"row":43,"column":51},"end":{"row":43,"column":52},"action":"insert","lines":["c"]},{"start":{"row":43,"column":52},"end":{"row":43,"column":53},"action":"insert","lines":["i"]},{"start":{"row":43,"column":53},"end":{"row":43,"column":54},"action":"insert","lines":["p"]},{"start":{"row":43,"column":54},"end":{"row":43,"column":55},"action":"insert","lines":["e"]},{"start":{"row":43,"column":55},"end":{"row":43,"column":56},"action":"insert","lines":["s"]},{"start":{"row":43,"column":56},"end":{"row":43,"column":57},"action":"insert","lines":["_"]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":24},"action":"remove","lines":["recipes_per_page = 4"],"id":926}],[{"start":{"row":42,"column":42},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":927},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":43,"column":4},"end":{"row":43,"column":24},"action":"insert","lines":["recipes_per_page = 4"],"id":928}],[{"start":{"row":46,"column":85},"end":{"row":46,"column":86},"action":"insert","lines":["s"],"id":929}],[{"start":{"row":46,"column":62},"end":{"row":46,"column":63},"action":"insert","lines":["s"],"id":930}],[{"start":{"row":45,"column":1},"end":{"row":45,"column":2},"action":"remove","lines":[" "],"id":931},{"start":{"row":45,"column":0},"end":{"row":45,"column":1},"action":"remove","lines":[" "]},{"start":{"row":44,"column":72},"end":{"row":45,"column":2},"action":"remove","lines":["","  "]}],[{"start":{"row":36,"column":0},"end":{"row":39,"column":0},"action":"remove","lines":["  ","    # recipes = mongo.db.recipes.find().sort('_id', -1).skip(","    # (page - 1)* recipes_per_page).limit(recipes_per_page)",""],"id":932},{"start":{"row":35,"column":12},"end":{"row":36,"column":0},"action":"remove","lines":["",""]},{"start":{"row":35,"column":8},"end":{"row":35,"column":12},"action":"remove","lines":["    "]},{"start":{"row":35,"column":4},"end":{"row":35,"column":8},"action":"remove","lines":["    "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"remove","lines":["    "]},{"start":{"row":34,"column":83},"end":{"row":35,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":353,"scrollleft":0,"selection":{"start":{"row":37,"column":42},"end":{"row":37,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":{"row":72,"state":"start","mode":"ace/mode/python"}},"timestamp":1567184906572,"hash":"fe6fc5ec794ef28173192855ae7e2956259b1444"}
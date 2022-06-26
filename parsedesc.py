def initialize():
    stackstring =  '''.NET,.NET Core,A11y,AES,AIML,AJAX,ALICE,APL,ASP,ASP.NET,AWS,ActionScript,Ada,Adobe,Adobe XD,Advanced Encryption Standard,After Effects,Airflow,Alibaba Cloud,Amazon EC2,Amazon ECR,Amazon EKS,Amazon EMR,Amazon ElastiCache,Amazon Glacier,Amazon Machine Learning,Amazon Route 53,Amazon S3,Amazon SageMaker,Amazon Simple Email Service,Amazon Simple Notification Service,Amazon Simple Queue Service,Amazon Simple Storage Service,Amazon Simple Workflow Service,Amazon Virtual Private Cloud,Amazon Web Services,Android,Android Studio,Angular,Angular.js,AngularJS,Ansible,Ant,Apollo,AppCode,AppDynamics,AppGameKit,AppVeyor,Arduino,Asana,Assembly,Athena,Atom,Auditbeat,Aurora,Avro,Azure,Azure DevOps,Azure Pipelines,Babel,Bamboo,Basecamp,Bash,BigQuery,Birst,Bitbucket Pipelines,BlockApps,Bootstrap,Brackets,C,C#,C++,CLion,COBOL,CSS,CSV,Calypso,Cassandra,ChatScript,Chef,CherryPy,Chuck,Cinder,CircleCI,Clickteam Fusion,Clojure,CloudBees,CodeBuild,CodeDeploy,CodePipeline,CoffeeScript,Confluence,Construct,Construct 2,Construct 3,Cordova,Couchbase,Dart,DataGrip,Datadog,DigitalOcean,Directx,Django,Docker,Domo,Dreamweaver,Drill,Dundas BI,DynamoDB,ESLint,Eclipse,Elasticsearch,Elixir,Emacs,Embark,Erlang,Excel,Expo,Express,Express.js,F#,FORTRAN,FastAPI,Filebeat,Fireworks,Flash,Flask,Flink,Flock,Flutter,Forth,Freenode,Functionbeat,GDevelop,GPT-3,GPT3,Game Salad,GameMaker,GameMaker Studio,Ganache,Geth,GitLab CI,Gitter,Glassfish,Go,GoLand,Godot,Godot Engine,GoodData,Google Cloud,Google Cloud Build,Google Data Studio,Google Sheets,Grafana,GraphQL,Groovy,HBase,HTML,Hadoop,Haskell,Heartbeat,Heroku,Hive,IBM Cognos,IRC,Illustrator,InDesign,InfluxDB,Informatica,Insomnia,IntelliJ IDEA,Ionic,JBoss,JSON,Jaeger,Java,JavaScript,Jenkins,JetBrains PyCharm,JetBrains Rider,JetBrains WebStorm,Jira,Julia,Kafka,Keybase,Kibana,Kinesis,Koa,Kotlin,Kubernetes,LabVIEW,Laravel,Lightroom,Linode,Linux,Lisp,Logo,Logstash,Looker,Lucene,MARYTTS,MATLAB,MariaDB,Matrix,Maven,Max/MSP,Memcached,MetaMask,Metal,Metricbeat,MicroStrategy,Microservices,Microsoft BI,Microsoft Visual Studio Code,Minitab,MobX,MongoDB,Mongoose,MySQL,Nagios,Nano,NativeScript,Neo4j,New Relic,Node,Node.js,OCaml,Objective C,Objective-C,Objective-J,Open Frameworks,OpenAI,OpenCCG,OpenGL,OpenTracing,Oracle Business Intelligence,PHP,Packetbeat,Pandorabots,Panorama Necto,Parity,Pascal,Pentaho,Perl,Photoshop,PhpStorm,PlayCanvas,Polly,PostgreSQL,Postman,Power BI,PowerShell,Prettier,Prisma,Processing,Prolog,Prometheus,Puppet,PureData,PyCharm,Pylons,Pyramid,Python,Qlik,QuickSight,R,RPG Maker,RPG Maker MZ,Rackspace,React,React Native,React Router,React.js,Redis,Redshift,Redux,Redux Saga,Redux Thunk,Rider,Riot,Rivescript,Ruby,Ruby on Rails,RubyMine,Rust,SAP Business Objects,SAS,SPSS,SQL,SQLite,Saltstack,Samza,Sanic,Scala,Scheme,Scratch,Selenium,SimpleDB,Smalltalk,Socket.IO,Solidity,Solr,Sonic Pi,Spark,Sploder,Splunk,Spring,Stata,StatsD,Stencyl,Storm,SuperCollider,Swagger,Swift,TIBCO,Tableau,Tableau Public,Tcl/Tk,TeamCity,TensorFlow,Terraform,TestRPC,Tomcat,Tornado,Travis,Trello,Truffle,Twine,Tynker,TypeORM,TypeScript,Unity,Unreal,VHDL,Vaadin,Vagrant,Vantara,Verilog,Vim,Visual Basic,Visual Basic .NET,Visual Studio,Visual Studio Code,Vue,Vue.js,Vulkan,Web3.js,WebAssembly,WebRTC,WebStorm,Weblogic,Webpack,WhatsApp,Windows,Winlogbeat,Wire,XML,Xcode,Yellowfin,Zabbix,dotnet,fish,iOS,iTerm2,jQuery,macOS,nodejs,pytorc,scikit,sklearn,tmux,zsh'''
    return stackstring.split(",")


techstack = initialize()

import re
def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(re.escape(w)), flags=re.IGNORECASE).search

def parseTechInDesc(desc):
    techlist = ""
    for x in techstack:
        if (bool(findWholeWord(x)(desc))):
            techlist = techlist + "," + x
    return techlist[1:]

def parseSalary(desc):
    salarylist = ""
    separate = desc.replace("-"," ").replace("~"," ").split()
    for x in separate:
        amounts = re.findall("\$[0-9,.]*|¥[0-9,.]*|£[0-9,.]*|€[0-9,.]*|R\$[0-9,.]*", x)
        for y in amounts:
            salarylist=salarylist+" or "+y
    return salarylist[4:]

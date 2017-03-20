# pluginmanager
Module to simplify plugin instantiation and configuration. 

  Module to handle plugins dispatch, config.
  Model is plugins are kept in hierarchy by 'category', beneath category are types:
  
  <package>/plugins/<category>/[<type>/<subtype/]<PluginName>.py
                              
Plugins initialized with ConfigParser object and a section name as arguments. The 
assumption is that the classes themselves know how to look up the info they need. 
It is also assumed that Singleton/non-Singleton decision is made during class initialization.
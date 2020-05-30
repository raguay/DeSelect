JsOsaDAS1.001.00bplist00�Vscript_�function grabFirstNested(arr) {
  if (arr.length <= 0 || !Array.isArray(arr[0])) {
    return arr;
  }

  return grabFirstNested(arr[0]);
}

function run(arg) {

  var sys = Application('System Events');

  var servicesRef = sys.processes['fman'].menuBars.menuBarItems.whose({
    name: { _contains: 'fman'}
  }, {ignorign: 'case'}).menus.menuItems.whose({
    name: { _contains: 'services'}
  }, {ignoring: 'case'}).menus.menuItems.name;

  var services = grabFirstNested(servicesRef());
  var list = "{";
  services.forEach(function(service, index) {
    list += "'name': '" + service + "',";
  });
  list += "'name': ''}";

  return list;
}                              � jscr  ��ޭ
$(document).ready(function() {

//----------------------------------------------------------
//     JS AJAX
//----------------------------------------------------------



// ------------------------------------------
//      Ajax Filtrar Listado Variedades
//  ------------------------------------------
    var formulariolistar = $('.listar_ajax');
        formulariolistar.bind('submit',function () {
            $.ajax({
                type: formulariolistar.attr('method'),
                url: formulariolistar.attr('action'),
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablacontenido").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });
       return false;
    });


    //mostrar sub grupos al seleccionar grupo
    $('#departamento').change(function(e){
         // alert(this.value);
         var url1='/filtrar_ciudades/'+this.value+'/' ;

       // alert(id_grupo);
       e.preventDefault();
       $.ajax({
        type: 'GET',
        url: url1,
        beforeSend: function(){
               // $('.preload_users').html('<img src="imgs/350.gif" />');
               // alert("va a enviar ajax");
           },
           complete: function(data){

           },
           success: function (data) {
                //$('.preload_users').html('');
                //$('.load_ajax').html(usuarios)
                // alert(data);
                // alert(data[1].pk)
                // alert(data[1].fields.nombre_lugar)
                var ciudades = '';  
                ciudades += '<option value="seleccionar">Seleccionar</option>';
                for (i in data) {

                   ciudades += '<option value="'+data[i].pk+'">';
                   ciudades +=  data[i].fields.nombre_lugar;
                   ciudades += '</option>';

               };

               $('#seleccionar_ciudades').html(ciudades);
                // $('#seleccionar_ciudades').html('<option value="seleccionar">Seleccionar SubGgrupo</option>');
            },
            error: function(errors){
                alert('no se ha creado');
            }
        })
    });


$('#categoria').change(function(e){
         // alert(this.value);
         var url1='/filtrar_categorias/'+this.value+'/' ;

       // alert(id_grupo);
       e.preventDefault();
       $.ajax({
        type: 'GET',
        url: url1,
        beforeSend: function(){
               // $('.preload_users').html('<img src="imgs/350.gif" />');
               // alert("va a enviar ajax");
           },
           complete: function(data){

           },
           success: function (data) {
                //$('.preload_users').html('');
                //$('.load_ajax').html(usuarios)
                // alert(data);
                // alert(data[1].pk)
                // alert(data[1].fields.nombre_lugar)
                var subcategoria = '';  
                subcategoria += '<option value="0">Seleccionar</option>';
                for (i in data) {

                 subcategoria += '<option value="'+data[i].pk+'">';
                 subcategoria +=  data[i].fields.nombre_cat_interna;
                 subcategoria += '</option>';

             };

             $('#subcategoria').html(subcategoria);
                // $('#seleccionar_ciudades').html('<option value="seleccionar">Seleccionar SubGgrupo</option>');
            },
            error: function(errors){
                alert('no se ha creado');
            }
        })
});




$('#categoriaAdd').change(function(e){
         // alert(this.value);
         var url1='/filtrar_categorias/'+this.value+'/' ;

       // alert(id_grupo);
       e.preventDefault();
       $.ajax({
        type: 'GET',
        url: url1,
        beforeSend: function(){
               // $('.preload_users').html('<img src="imgs/350.gif" />');
               // alert("va a enviar ajax");
           },
           complete: function(data){

           },
           success: function (data) {
                //$('.preload_users').html('');
                //$('.load_ajax').html(usuarios)
                // alert(data);
                // alert(data[1].pk)
                // alert(data[1].fields.nombre_lugar)
                var subcategoria = '';  
                subcategoria += '<option value="0">Seleccionar</option>';
                for (i in data) {

                 subcategoria += '<option value="'+data[i].pk+'">';
                 subcategoria +=  data[i].fields.nombre_cat_interna;
                 subcategoria += '</option>';

             };

             $('#subcategoriaAdd').html(subcategoria);
                // $('#seleccionar_ciudades').html('<option value="seleccionar">Seleccionar SubGgrupo</option>');
            },
            error: function(errors){
                alert('no se ha creado');
            }
        })
});

//----------------------------------------------------------
//     JS INTERFAZ GRAFICA USUARIOS VENDEDOR
//----------------------------------------------------------


    // Funcion al seleccionar permisos check box
    $("#administrador").change(function() { 
        if($("#administrador").is(':checked')) { 

            $('#catalogo').attr('disabled','disabled');
            $("#catalogo").prop('checked', true);

            $('#pedidos').attr('disabled','disabled');
            $("#pedidos").prop('checked', true);

            $('#reportes').attr('disabled','disabled');
            $("#reportes").prop('checked', true);

            

        }else{

            $('#catalogo').removeAttr('disabled');
            $("#catalogo").prop('checked', false);

            $('#pedidos').removeAttr('disabled');
            $("#pedidos").prop('checked', false);

            $('#reportes').removeAttr('disabled');
            $("#reportes").prop('checked', false);
            

        }
    }); 


    $('.eliminar_usuarios').click(function(){

         $('#nombre_eliminar').html($(this).attr('nombre'));
         $('#apellido_eliminar').html($(this).attr('apellido'));
         $('#email_eliminar').html($(this).attr('email'));
         $('#username_eliminar').html($(this).attr('usuario'));
         $('#pk_eliminar').val($(this).attr('usuario'));




    });

    $('.eliminar_productos').click(function(){

         $('#nombre_eliminar').html($(this).attr('nombre'));
         $('#subcategoria_eliminar').html($(this).attr('subcategoria'));
         $('#precioCompra_eliminar').html($(this).attr('precioCompra'));
         $('#precioVenta_eliminar').html($(this).attr('PrecioVenta'));
         $('#descuento_eliminar').html($(this).attr('descuento'));
         $('#iva_eliminar').html($(this).attr('iva'));
         $('#descripcion_eliminar').html($(this).attr('descripcion'));
         $('#imagen_eliminar').html($(this).attr('imagen'));
         $('#presentacion_eliminar').html($(this).attr('presentacion'));
         $('#empresa_eliminar').html($(this).attr('empresa'));
         $('#pk_eliminar').val($(this).attr('producto'));
    });


$('#buscarUsuarioComprador').keyup(function() {
    var formulariolistar = $('.listar_ajax');
       $.ajax({
                type:'post',
                url: '/filtroCompradorUsuarios/',
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablacontenido").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });
});    



$('#buscarUsuarioCompradorV').keyup(function() {
    var formulariolistar = $('.listar_ajaxV');
       $.ajax({
                type:'post',
                url: '/filtroCompradorUsuariosV/',
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablacontenido").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });
});    


$('#selectTipo').change(function(){
     var formulariolistar = $('.listar_ajax');
       $.ajax({
                type:'post',
                url: '/filtroCompradorUsuarios/',
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablacontenido").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });

});



$('#selectTipoV').change(function(){
     var formulariolistar = $('.listar_ajaxV');
       $.ajax({
                type:'post',
                url: '/filtroCompradorUsuariosV/',
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablacontenido").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });

});

//catalogo


$('#categoria').change(function(){
     var formulariolistar = $('.formaCatalogoAjax');
       $.ajax({
                type:'post',
                url: '/filtroVendedorCatalogo/',
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablaCatalogo").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });

});


$('#subcategoria').change(function(){
     var formulariolistar = $('.formaCatalogoAjax');
       $.ajax({
                type:'post',
                url: '/filtroVendedorCatalogo/',
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablaCatalogo").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });

});


$('#productoBuscar').keyup(function(){
     var formulariolistar = $('.formaCatalogoAjax');
       $.ajax({
                type:'post',
                url: '/filtroVendedorCatalogo/',
                data: formulariolistar.serialize(),
                beforeSend: function(){

                },
                complete: function(data){
                    
                },
                success: function (data) {
                    $('.eliminar').remove();

                    $("#tablaCatalogo").append(data);
  
                },
                error: function(errors){
                    alert('no se ha creado');
                }
            });

});

//----------------------------------------------------------
//     JS INTERFAZ GRAFICA REGISTRO
//----------------------------------------------------------


$('#label-switch').on('switch-change', function(e,data){
    if (data.value==false) {
        $('#codigo-form').remove();
        $("select option[value='Comprador']").attr("selected","selected");

    } else{
        $("#codigo-before").append('<div class="control-group" id="codigo-form"><label class="control-label" for="codigo-input">NIT</label><div class="controls"><input type="number" id="codigo-input" name="nit" required></div></div>');
        $("select option[value='Vendedor']").attr("selected","selected");

    }
});



// if (document.getElementById("#label-check").checked) {
//     $("#codigo-before").append('<div class="control-group" id="codigo-form"><label class="control-label" for="codigo-input">NIT</label><div class="controls"><input type="number" id="codigo-input" name="nit" required></div></div>');
//     $("select option[value='Ambos']").attr("selected","selected");
// };

// '''
// Autor           Jhonatan Acelas Arevalo 
// Fecha           23 Julio 2015
// Descripcion     validar que se seleccione al menos un permiso en modificar y agregar usuarios
// Funcion         Vendedores.compradres.1
// '''


    var checkboxes = $('.require-one');
    var checkbox_names = $.map(checkboxes, function(e, i) {
        return $(e).attr("name")
    }).join(" ");
    
    $("#itemForm").validate({
        groups: {
            checks: checkbox_names
        },
        rules: {
            
        },
        messages: {
            
        },
        errorPlacement: function(error, element) {
            $('#form_error').append(error);
            $('#form_error').html('<div class="alert alert-danger" role="alert"><span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span><span class="sr-only">Error: </span>Seleccione al menos un Permiso</div>');

        }
        // ,
        // submitHandler: function(form) {
        //     alert('Form Submited puta alerta');
        //     return false;
        // }        
    
    });





});

// '''
// Autor           Jhonatan Acelas Arevalo 
// Fecha           23 Julio 2015
// Descripcion     validar que se seleccione al menos un permiso en modificar y agregar usuarios
// Funcion         Vendedores.compradres.1
// '''

$.validator.addMethod('require-one', function(value) {
    if (true) {
        return $('.require-one:checked').size() > 0;
    } else {
        return true;
    }
}, 'Seleccione un permiso.');





function validarCategoria(form) 
    { 
        
        if (form.categoria.options[form.categoria.selectedIndex].value == 0){
            alert("Debe seleccionar una categoria");
            return false;
        }
        if (form.subcategoria.options[form.subcategoria.selectedIndex].value == 0){
            alert("Debe seleccionar una subcategoria");
            return false;
        }
        return true;
    }  



 